from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    return BFS(begin, target, words)

def BFS(begin, target, words):
    queue = deque()
    queue.append([0, begin])
    
    while queue:
        step, status = queue.popleft()
        
        if status == target:                # 먼저 사전 실행
            return step
        
        for word in words:
            cnt = 0
            for i in range(len(begin)):
                if word[i] != status[i]:    # HIT => HOT
                           cnt +=1
            if cnt == 1:
                queue.append([step+1, word])
                           
                           
