# This function calcultes the determinant of any sqauare matrix
'''
import math

order = 4
    
a1 = [1,2,3,5]
a2 = [1,4,9,25]

a3 = [1,8,27,125]
a4 = [1,16,81,625]


c0=(1+math.sqrt(3))/4*math.sqrt(2)
c1=(3+math.sqrt(3))/4*math.sqrt(2)
c2=(3-math.sqrt(3))/4*math.sqrt(2)
c3=(1-math.sqrt(3))/4*math.sqrt(2)
a1 = [c0,c1,c2,c3]
a2 = [c2,c3,c0,c1]
a3 = [c3,-c2,c1,-c0]
a4 = [c1,-c0,c3,-c2]


result = ( a1[0]*(  a2[1] * (a3[2]*a4[3] - a3[3]*a4[2])
                  - a3[1] * (a2[2]*a4[3] - a2[3]*a4[2])
                  + a4[1] * (a2[2]*a3[3] - a2[3]*a3[2])
                  )
          -a2[0]*(  a1[1] * (a3[2]*a4[3] - a3[3]*a4[2])
                  - a3[1] * (a1[2]*a4[3] - a1[3]*a4[2])
                  + a4[1] * (a1[2]*a3[3] - a1[3]*a3[2])
                  )
          +a3[0]*(  a1[1] * (a2[2]*a4[3] - a2[3]*a4[2])
                  - a2[1] * (a1[2]*a4[3] - a1[3]*a4[2])
                  + a4[1] * (a1[2]*a2[3] - a1[3]*a2[2])
                 )
          -a4[0]*(  a1[1] * (a2[2]*a3[3] - a2[3]*a3[2])
                  - a2[1] * (a1[2]*a3[3] - a1[3]*a3[2])
                  + a3[1] * (a1[2]*a2[3] - a1[3]*a2[2])
                 )
         )
'''
def getCofactor(rowPred, CurCol):   # Get cofactor for the current row and column
                                    # rowPred contains the list of row numbers for the hiarrchy                                   
    maxindex = Dimension - 1
    j = 0
    result = 0 
    for i in range (Dimension):
        if i not in rowPred:
            if CurCol == maxindex:
                return matrix[i][CurCol]
            else:
                j += 1
                rowList = []
                for k in range(len(rowPred)):
                    rowList.append(rowPred[k])  
                rowList.append(i)
                if j%2 > 0:
                    cof = getCofactor (rowList, CurCol + 1)
                    result += matrix[i][CurCol] * cof
                else:
                    cof = getCofactor (rowList, CurCol + 1)
                    result += (-1) * matrix[i][CurCol] * cof
    return result

#matrix = [[2,4,8,16],[3,9,27,81],[1,1,1,1],[5,25,125,625]]
#matrix = [[12,4,3],[8,-12,-9],[33,-4,-24]]
Dimension = len(matrix)
result = getCofactor([], 0)

print ('det = ', result)

