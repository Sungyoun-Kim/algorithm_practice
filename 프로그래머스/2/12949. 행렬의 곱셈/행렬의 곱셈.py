def solution(arr1, arr2):
    row_len = len(arr1)
    col_len1 = len(arr1[0])
    col_len2 = len(arr2[0])
    
    answer = [[0 for _ in range(col_len2)] for _ in range(row_len)]
    
    for i in range(row_len):
        for j in range(col_len2):
            for k in range(col_len1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer