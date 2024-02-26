def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer

def DFS(n, computers, com, visited):        # 이전 값 : com, 최근 값 : connect
    visited[com] = True
    for connect in range(n):
        if com != connect and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

