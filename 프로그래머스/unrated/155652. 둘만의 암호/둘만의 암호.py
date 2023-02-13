#1
def solution(s,skip,index):
    res = ''
    #'a'~'z'까지 중 skip에 없는 리스트 arr --> skip에 있는 문자들을 건너뛸 수 있음
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    # '% len(arr)'를 한 이유 --> index를 더해주고 나서 'z', 122를 넘게되면 다시 'a'로 돌아가 순환하기 위함 
    for i in s:
        res += arr[(arr.index(i) + index) % len(arr)]

    return res

#2
#ascii코드 사용을 위한 라이브러리 import
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''
    #ascii_lowercase --> 소문자 알파벳(정렬되어 있지x)
    a_to_z = set(ascii_lowercase)
    #skip에 있는 문자를 제외한 알파벳
    a_to_z -= set(skip)
    #정렬(list)
    a_to_z = sorted(a_to_z)

    #딕셔너리 --> {값:인덱스}
    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % len(a_to_z)]
    
    return result
