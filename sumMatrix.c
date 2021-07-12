#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
#include<unistd.h>
#include<errno.h>
#include<ctype.h>
#include<stdlib.h>

#define NUMROW 958

#define NUMCOL 9

#define MAXNUM 1000

#define handle_error_en(en,msg) \
	do { errno=en; perror(msg); exit(EXIT_FAILURE); } while(0)

#define handle_error(msg) \
	do { perror(msg); exit(EXIT_FAILURE); } while(0)

/* global matrix and sum array to be accessed by all counting threads */

int matrix[NUMROW][NUMCOL];  

int sums[NUMCOL];

struct thread_info{ 	/* Used as argument to counting_threads() */
	pthread_t thread_id;
	int 	  thread_num;
};
	
sem_t lock[NUMCOL];

void *sum_thread(void *arg)
{
 	struct thread_info *tinfo=arg;
 	int i=0,sum=0,s;
 	                    
    	for (i = 0; i < NUMROW; i++) 
        	sum = sum+ matrix[i][tinfo->thread_num];
	
	printf("T%d = %d\n",tinfo->thread_num,sum);
	
	if (0 == tinfo->thread_num){ 
		sums[tinfo->thread_num]=sum;
	} else {
#ifdef SYNCHRONISE
        	if (0 != (s=sem_wait(&lock[tinfo->thread_num-1])))
			handle_error_en(s,"sem_wait");
#endif

		sums[tinfo->thread_num] = sums[tinfo->thread_num -1] + sum;
	}	
	if (tinfo->thread_num<8){
#ifdef SYNCHRONISE        
        	if (0!=(s= sem_post(&lock[tinfo->thread_num])))
			handle_error_en(s,"sem_post");
#endif
	}
	
	return (void *) tinfo;
}

int main(int ac, char *av[])
{
	int roll=2005,s;
	int row,col;
	struct thread_info *tinfo;
	
	/* create matrix with random numbers in range [0,1000} */
		
    	srand(roll);
    	for (row=0;row<NUMROW;row++){
    		for (col=0;col<NUMCOL;col++){
    			matrix[row][col]=rand()%MAXNUM; 
    		}
    	}
	
	/* initialise all semaphores to 0 */
	for (col=0;col<NUMCOL;col++){ 
		if (0!=(s= sem_init(&lock[col], 0, 0)))
			handle_error_en(s,"sem_init");
	} 
 	/* allocate space for thread_info */
	if (NULL==(tinfo=calloc(NUMCOL,sizeof(struct thread_info)))){
		handle_error("calloc");
	}

	/* Create threads for counting each column of the matrix */
	for (col=0;col<NUMCOL;col++){
		tinfo[col].thread_num=col; 
		/* The pthread_create() call stores the thread id to corresponding 
		   element of tinfo[] */
		   
		if (0!=(s=pthread_create(&tinfo[col].thread_id,NULL,&sum_thread,&tinfo[col]))){
			handle_error_en(s,"pthread_create");
		} 
	}

	/* Wait for 1 minute for counting threads to complete */
	sleep(2);
		
	/* Now join the threads and print final sum */

	for (col=0;col<NUMCOL;col++){
		if(0!=(s=pthread_join(tinfo[col].thread_id, NULL))){
			handle_error_en(s,"pthread_join");
		}
	}
	printf("%d\n",sums[8]); /* print the total sum of the matrix */
	free (tinfo);
	exit(EXIT_SUCCESS);

    	return 0;
    	
    	/*  If this program is compiled without DSYNCHONISED option (i.e. not using semaphores for checking 
        if earlier column calculations are done, before cummulating current column ,
        then minimum value of sum can be 0 (the minimum possible sum for column 8 alone, 
        if thread for summing column 8 runs first)
        maximum value of sums[8] can be 9*958*999=8613378 */
}

