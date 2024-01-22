#BFS => 너비 우선 탐색
def solution(numbers, target):
    leaves = [0]                # 자식 노드들
    cnt = 0
    for number in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + number)  # 0 + 4, 4 + 1, -4 + 1
            temp.append(leaf - number) # 0 - 4, 4 -1, -4 -1
        
        leaves = temp          # [4 , -4]
    
    for leaf in leaves:
        if leaf == target:
            cnt += 1
            
    return cnt

#DFS => 깊이 우선 탐색
# def dfs(numbers, target, idx, values):
#     global cnt      # 전역함수
#     cnt = 0
    
#     if idx == len(numbers) & values == target:
#         cnt += 1
#         return
#     elif idx == len(numbers):                       # 끝까지 탐색했는데 target과 다를 때
#         return                            # 아무일 없이 
    
#     dfs(numbers, target, idx+1, values + numbers[idx])          # 더하기
#     dfs(numbers, target, idx+1, values - numbers[idx])          # 빼기
    
    
# def solution(numbers,target):
#     global cnt
#     dfs(numbers,target,0,0)
    
#     return cnt
    
    