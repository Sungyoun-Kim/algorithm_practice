import sys

if __name__ == "__main__":
    S = int(sys.stdin.readline())
    count = 0
    sum=0
    for i in range(S):
        if sum+i+i+1> S:
            break
        sum=sum+i
        count+=1
    print(count)
