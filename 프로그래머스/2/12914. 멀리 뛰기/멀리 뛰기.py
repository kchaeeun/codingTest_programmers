# 규칙) 피보나치 배열 [1, 2, 3, 5, 8..] 이런식으로 경우의 수 증가! => n값이 늘어날 떄마다 경우의 수를 직접 작성.
# def solution(n):
#     answer = 0
#     l = [1] * n
#     for i in range(1,n):
#         l[i] = l[i-2]+l[i-1] 
        
#     answer = l[-1] % 1234567
#     return answer

def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    l = [0] * n
    l[0] = 1
    l[1] = 2
    
    for i in range(2, n):
        l[i] = l[i-2] + l[i-1]
    
    answer = l[-1] % 1234567
    return answer