from collections import deque
def solution(maps):
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0,0,1)])
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == n -1 and y == m -1:      # 정점이 목표지점에 도달 시 (n,m)
            return cnt
        for dx, dy in directions:
            nx, ny = x + dx, y + dy     # 이동 중
            
            # 도착하지 않을 때
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
        
        
    return -1