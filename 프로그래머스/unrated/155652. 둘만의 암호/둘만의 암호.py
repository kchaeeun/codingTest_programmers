def solution(s,skip,index):
    res = ''
    #'a'~'z'까지 중 skip에 없는 리스트 arr --> skip에 있는 문자들을 건너뛸 수 있음
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    # '% len(arr)'를 한 이유 --> index를 더해주고 나서 'z', 122를 넘게되면 다시 'a'로 돌아가 순환하기 위함 
    for i in s:
        res += arr[(arr.index(i) + index) % len(arr)]

    return res