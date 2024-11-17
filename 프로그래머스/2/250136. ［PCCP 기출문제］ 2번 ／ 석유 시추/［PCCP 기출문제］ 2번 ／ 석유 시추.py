from collections import deque
def solution(land):
    answer = 0
    rows = len(land)
    cols = len(land[0])
    visited = [[False] * cols for c in range(rows)]
    col_oils = [0] * cols
    # print(col_oils)

    # print(visited) 
    def bfs(x,y):
        queue = deque([(x,y)])
        visited[x][y] = True
        oil_size = 0
        oil_col = set()

        while queue:
            cx, cy = queue.popleft()
            oil_size += 1           # 좌표 값이 1이기 때문
            oil_col.add(cy)         # 오일이 있는 열(y) 값 추가 (<-> 행은 x)

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))


        return oil_size, oil_col

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and land[i][j] == 1:
                size, cols_set = bfs(i,j)
                for c in cols_set:
                    col_oils[c] += size

    return max(col_oils)