def solution(answers):
    answer = {1:0, 2:0, 3:0}
    num = {1:[1,2,3,4,5], 2: [2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    
    for i in range(1,4):
        if len(answers) > len(num[i]):
            num[i] = num[i] * (len(answers) // len(num[i]) +1)

    for i in range(1,4):
        for j in range(len(answers)):
            if answers[j] == num[i][j]:
                answer[i] += 1
    
    # first.append(first[:len(first) % len(answers)])
    res = [0]
    max_n = 0
    for i in range(1,4):
        if max_n < answer[i]:
            max_n = answer[i]
            res[0]=i

        elif res[0] != 0 and max_n == answer[i]:
            res.append(i)

    sorting = sorted(res)        

    return sorting