def solution(clothes):
    # answer = len(clothes)
    cnt = 1
    dic = {}
    for i in range(len(clothes)):
                  dic[clothes[i][1]] = []
    for i in range(len(clothes)):
                   dic[clothes[i][1]].append(clothes[i][0])

    for i in dic:
        cnt *= len(dic[i]) + 1
    cnt -= 1
    return cnt