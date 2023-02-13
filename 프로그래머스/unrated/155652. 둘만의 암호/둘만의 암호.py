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