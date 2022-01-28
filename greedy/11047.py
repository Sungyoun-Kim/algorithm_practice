import sys

if __name__ == "__main__":
    N, K = map(int,sys.stdin.readline().split())
    coin = []
    for i in range(N):
        coin.append(int(sys.stdin.readline()))
    coin.reverse()
    count = 0
    while K != 0:
        if coin[0] > K:
            del coin[0]
            continue
        if not coin:
            break
        K = K - coin[0]
        count += 1


    print(count)

