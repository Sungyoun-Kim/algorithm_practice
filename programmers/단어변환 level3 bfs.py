from collections import deque


def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    queue = deque()
    queue.append([begin, 0])
    answer = 0;
    while queue:
        x, y = queue.popleft()
        if x == target:
            answer = y
            break
        for i in range(len(words)):
            diff = 0
            if not visited[i]:
                for j in range(len(x)):
                    if x[j] != words[i][j]:
                        diff = diff + 1
                if diff == 1:
                    queue.append([words[i], y + 1])
                    visited[i] = 1
    return answer




