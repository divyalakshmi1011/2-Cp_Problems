# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    # print("divya")
    r1 = len(m1)
    c1 = len(m1[0])

    r2 = len(m2)
    c2 = len(m2[0])
    # print(r1,c1,r2,c2)
    if c1 != r2:
        return None
    else :
        c = [[0 for h in range(len(m2[0]))] for l in range(len(m1))] 
        
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    print(m1[i][k], m2[k][j])
                    c[i][j] += (m1[i][k] * m2[k][j])
                    # print(c[i][j])
        return c

print(fun_matrixmultiply([[1, 3], [2, 4]], [[1, 3, 2, 2], [2, 4, 5, 1]]))




