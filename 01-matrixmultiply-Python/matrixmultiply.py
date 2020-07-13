# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    r1 = len(m1)
    c1 = len(m1[0])

    r2 = len(m2)
    c2 = len(m2[0])
    if c1 != r2:
        return None
    else :
        c = []
        for h in range(c1):
            for l in range(r2):
                c[h][l] = 0
        for i in range(r1):
            for j in range(c2):
                for k in range(r2):
                    c[i][j] += m1[i][k] * m2[k][j]
        return c




