import sys  

N = int(sys.stdin.readline())
ans = 0

col   = [False] * N       
diag1 = [False] * (2*N-1) 
diag2 = [False] * (2*N-1) 

def backtrack(r: int) -> None:
    global ans
    if r == N:       
        ans += 1
        return
    for c in range(N):
        d1 = r + c
        d2 = r - c + N - 1
        if col[c] or diag1[d1] or diag2[d2]:
            continue        
        col[c] = diag1[d1] = diag2[d2] = True
        backtrack(r + 1)
        col[c] = diag1[d1] = diag2[d2] = False

backtrack(0)
print(ans)