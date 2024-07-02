# computer[i][i] = 1 computers는 번호가 정해져있다.
# computer[i][j] = 1 연결되어있다.
def solution(n, computers):
    answer = 0
    visit = [[0 for _ in range(n)]for _ in range(n)]

    def dfs(com_num):
        global find_network_flag
        for c in range(n):
            if computers[com_num][c] == 1 and visit[com_num][c] ==0:
                visit[com_num][c] = 1
                visit[c][com_num] =1
                find_network_flag = True
    
                dfs(c)
    for i in range(n):
        global find_network_flag 
        find_network_flag = False
        dfs(i)
        if find_network_flag:
            answer+=1
            
    return answer
            
            
                
                
        
    
        
    return answer