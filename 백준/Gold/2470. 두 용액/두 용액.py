import sys

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    liquids = list(map(int,sys.stdin.readline().split()))
    liquids.sort()
    acidity = 1e10+1
    left = 0
    right = N-1
    result = []
    while left < right:
        if abs(liquids[left] + liquids[right]) < acidity:
            acidity = abs(liquids[left] + liquids[right])
            result = [liquids[left],liquids[right]]
        if liquids[left]+liquids[right] >0 :
            right-=1
        else:
            left+=1
    print(result[0],result[1])







