import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    C=[]
    for i in range(T):
        C.append((int(sys.stdin.readline())))

    result = []
    for i in C:
        quarter = i// 25
        dime = (i%25)//10
        nickel = ((i%25)%10)//5
        penny = (((i%25)%10)%5)//1
        result.append([quarter,dime,nickel,penny])

    for i in result:
        for j in i:
            print(j,end=' ')
        print('')


