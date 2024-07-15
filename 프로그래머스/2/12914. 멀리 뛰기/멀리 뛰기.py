def solution(n):
    answer = 0
    l = [1] * (n)
    for i in range(1,n):
        l[i] = l[i-2]+l[i-1] 
        
    answer = l[-1] % 1234567
    return answer