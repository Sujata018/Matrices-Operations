# This function calcultes the determinant of any sqauare matrix of any dimension
#
# Enter your matrix in list form in lines 32, like below, and run the program to get determinant.
# matrix = [[12,4,3],[8,-12,-9],[33,-4,-24]]
##

import math

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

#matrix = [[2,4,8,16],[3,9,27,81],[1,1,1,1],[5,25,125,625]]   # 4 x 4 matrix structure
matrix = [[12,4,3],[8,-12,-9],[33,-4,-24]]    # 3 x 3 matrix structure
Dimension = len(matrix)
result = getCofactor([], 0)

print ('det = ', result)

