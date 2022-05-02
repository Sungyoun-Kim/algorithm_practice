
import sys
sys.setrecursionlimit(100000)



def dfs(node,parent):

    parent_arr[node] = parent
    for i in tree[node]:
        if i == parent:
            continue
        dfs(i,node)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]

    parent_arr = [0 for _ in range(N+1)]

    for i in range(N - 1):
        node1, node2 = map(int, sys.stdin.readline().split())
        tree[node1].append(node2)
        tree[node2].append(node1)
    dfs(1,0)

    for i in range(2,N+1):
        print(parent_arr[i])




"""
트리의 부모 찾기 성공
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	38601	16674	12035	42.209%
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
출처
문제를 만든 사람: baekjoon
잘못된 조건을 찾은 사람: jh05013
알고리즘 분류
그래프 이론
그래프 탐색
트리
너비 우선 탐색
깊이 우선 탐색"""