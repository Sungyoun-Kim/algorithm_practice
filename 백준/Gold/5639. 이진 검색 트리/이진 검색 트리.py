import sys
sys.setrecursionlimit(100000)
def postOrder(start,end):

    if start>end:
        return

    mid =end+1
    for i in range(start+1,end+1):
        if preOrderResult[i] > preOrderResult[start]:
            mid = i
            break


    postOrder(start+1,mid-1)
    postOrder(mid,end)
    print(preOrderResult[start])




if __name__ =="__main__":
    preOrderResult = []

    while True:
        try:
            preOrderResult.append(int(sys.stdin.readline()))
        except:
            break
    postOrder(0,len(preOrderResult)-1 )




