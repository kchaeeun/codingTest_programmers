#1
def solution(s):
    #문자열 자체도 list이기에 인덱스 사용이 가능하다.
    answer = ''
    #lst = [i for i in s]
    if len(s) % 2 == 0:
        answer = s[(len(s)//2)-1] + s[(len(s)//2)]
        
    else:
        answer = s[(len(s)//2)]
        
    return answer 
#2
def solution(s):
    #slicing 사용
    return s[(len(s)-1)//2 : len(s)//2 + 1]
