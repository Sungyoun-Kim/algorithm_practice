
def solution(m, n, puddles):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in puddles:
        matrix[i[1]-1][i[0]-1] =-1
    matrix[0][0 ] =1
    for i in range(n):
        if matrix[i][0]==-1:
            break
        matrix[i][0]=1
    for i in range(m):
        if matrix[0][i]==-1:
            break
        matrix[0][i]=1

    for i in range(1,n):
        for j in range(1 ,m):
            if matrix[i][j]==-1:
                continue
            if matrix[i-1][j] == -1 and matrix[i][j - 1] != -1:
                matrix[i][j] = matrix[i][j-1]
            elif matrix[i][j-1] == -1 and matrix[i-1][j] != -1:
                matrix[i][j] = matrix[i-1][j]
            elif matrix[i - 1][j] != -1 and matrix[i][j - 1] == -1:
                matrix[i][j] = matrix[i - 1][j]
            elif matrix[i-1][j]==-1 and matrix[i][j-1]==-1:
                matrix[i][j]=0
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[n-1][m-1]%1000000007