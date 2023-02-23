def solution(clothes):
    arr = dict()
    for i in clothes:
        if i[1] in arr:
            # arr[key].append(value) ==> 'key' : [value]
            arr[i[1]].append(i[0])
        else:
            # dict에서 key값이 없는 경우 keyerror를 넘어가기 위해 사용
            # 새롭게 값을 넣어
            arr.setdefault(i[1],[i[0]])
    print(arr)

    v=[]

    for i in arr.values():
        v.append(len(i)+1)
    print(v)
    s = 1

    for i in v:
        s *= i
    
    s -= 1

    return s  