from collections import deque
def solution(begin, target, words):

    if target not in words:         # targetdl words 안에 없다면 반환할 수 없습니다.
        return 0
    
    return BFS(begin, target, words)

def BFS(begin, target, words):
    queue = deque()
    queue.append([begin, 0])        # 시작 단어와 단계 0(return 값, 변환 횟수)으로 초기화
    
    while queue:
        now, step = queue.popleft() 
        print(now, step)
        
        if now == target:
            return step
        
        for word in words:
            cnt = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    cnt += 1
            
            if cnt == 1:      # 1개만 다르다면(hit -> hot)
                queue.append([word, step+1])
    