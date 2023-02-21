#1.
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
        
    if len(answer) == 0 :
        answer.append(-1)
        
    answer.sort()
    return answer

#2.
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]