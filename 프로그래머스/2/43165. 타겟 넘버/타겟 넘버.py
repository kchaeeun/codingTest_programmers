def solution(numbers, target):
    DFS(numbers, target, 0, 0)
    return cnt

cnt = 0
def DFS(numbers, target, idx, values):
    global cnt
    
    if (idx == len(numbers)) and (values == target):
        cnt += 1
        return
    elif idx == len(numbers):       # target을 못찾음
        return
    
    DFS(numbers, target, idx+1, values + numbers[idx])
    DFS(numbers, target, idx+1, values - numbers[idx])
    