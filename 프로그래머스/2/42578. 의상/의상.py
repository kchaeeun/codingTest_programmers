def solution(clothes):
    cnt = 1
    dic = {}
    for i in range(len(clothes)):
                  dic[clothes[i][1]] = []
    for i in range(len(clothes)):
                   dic[clothes[i][1]].append(clothes[i][0])

    for i in dic:
        cnt *= len(dic[i]) + 1 # (a 종류의 개수 + 1) * (b 종류의 개수 + 1)
    cnt -= 1
    return cnt

# hash 사용하기
def solution(clothes):
    hash_map = {}
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type,0) + 1 # type에 해당하는 count를 새어준다. (기본값이 0)
    answer = 1
    print(hash_map)
    for type in hash_map:
        answer *= (hash_map[type] + 1)
        
    return answer - 1