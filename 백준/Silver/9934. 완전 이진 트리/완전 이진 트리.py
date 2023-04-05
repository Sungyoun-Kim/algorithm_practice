import sys
import math

def createTree(start,end,level):

    if level == K:
        return
    parentNodeIdx = (start+end) //2

    treeLevel[level].append(sequence[parentNodeIdx])
    createTree(start,parentNodeIdx,level+1)
    createTree(parentNodeIdx,end,level+1)


if __name__ =="__main__":
    K = int(sys.stdin.readline())
    sequence = list(map(int,sys.stdin.readline().split()))
    treeLevel = [[] for _ in range(K)]
    createTree(0,len(sequence),0)

    for i in treeLevel:
        for j in i:
            print(j,end=' ')
        print()



