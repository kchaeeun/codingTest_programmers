def solution(a, b):
    answer = 0
    if a < b:
         answer = sum(range(a,b+1))
    elif a == b:
        answer = a
    else:
        answer = sum(range(b,a+1))
            
    return answer