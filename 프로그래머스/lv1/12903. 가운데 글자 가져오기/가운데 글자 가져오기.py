def solution(s):
    answer = ''
    lst = [ i for i in s]
    if len(lst) % 2 == 0:
        answer = lst[(len(lst)//2)-1] + lst[(len(lst)//2)]
        
    else:
        answer = lst[(len(lst)//2)]
        
    return answer 