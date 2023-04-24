import sys
import copy

sys.setrecursionlimit(100000)

def findAnscestor(start,a, b):
    global node1Path
    global  node2Path
    global  isEnd

    if isEnd:
        return

    for i in tree[start]:
        path.append(i)
        if i == a:
            node1Path = copy.deepcopy(path)
        if i == b:
            node2Path = copy.deepcopy(path)
        if len(node1Path) > 0 and len(node2Path) > 0 and not isEnd:
            isEnd = True
            for j in range(10001):
                if len(node1Path) ==j or len(node2Path) == j:
                    print(node1Path[j-1])
                    return

                elif node1Path[j] != node2Path[j]:
                    print(node1Path[j-1])
                    return
        else:
            findAnscestor(i, a, b)
            path.pop()



if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        tree = [[] for _ in range(N+1)]

        treeForRoot = [[] for _ in range(N+1)]
        for _ in range(N-1):
            A, B = map(int, sys.stdin.readline().split())
            tree[A].append(B)
            treeForRoot[B].append(A)

        node1, node2 = map(int, sys.stdin.readline().split())

        rootNode = treeForRoot[1:].index([])+1
        path =[]
        node1Path = []
        node2Path = []
        isEnd = False
        path.append(rootNode)
        findAnscestor(rootNode,node1,node2)
        if not isEnd:
            print(rootNode)














