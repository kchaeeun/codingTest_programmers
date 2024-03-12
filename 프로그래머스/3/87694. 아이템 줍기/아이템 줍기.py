from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1]*102 for _ in range(102)]      #?
    visited = [[0]*102 for _ in range(102)]
    
    # 길이가 1인 모든 선분 저장
    edges = set()
    for elem in rectangle:
        lx, ly, rx, ry = map(lambda x:x*2, elem)        # 2차원 배열의 각 값에 *2
        for i in range(lx, rx+1):
            for j in range(ly, ry+1):
                if lx <i<rx and ly < j < ry:
                    graph[i][j] = 0
                elif graph[i][j] != 0 :
                    graph[i][j] = 1
                      
    dxs = [0,0,1,-1]        #?
    dys = [1,-1,0,0]
    queue = deque()
    queue.append((characterX*2, characterY*2))
    
    while queue:
        x, y = queue.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y]//2       # character와 item이 같은 좌표에 있을 수는 없다
            break
        for dx, dy in zip(dxs, dys):
            print(dx, dy)
            nx, ny = dx + x, dy + y     # 상하좌우로 이동

            if 0 < nx < 102 and 0 < ny < 102 and not visited[nx][ny]:       # visited가 1이 아니라면
                if graph[nx][ny] == 1:              # 선에 위치한 좌표라면
                    visited[nx][ny] = visited[x][y] + 1     # 경로 추가, x와 y는 character의 위치
                    queue.append((nx, ny))
    return answer
                    
                
    