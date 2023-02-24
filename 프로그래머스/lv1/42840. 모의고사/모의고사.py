def solution(answers):
    # 수포자들의 점수
    score = {1:0, 2:0, 3:0}
    # 수포자들의 패턴 저장
    pattern = {1:[1,2,3,4,5], 2: [2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    
    for i in range(1,4):
        # answers 길이에 따른 패턴 길이 늘리기
        if len(answers) > len(pattern[i]):
            pattern[i] = pattern[i] * (len(answers) // len(pattern[i]) +1)
        
        # 점수 저장
        for j in range(len(answers)):
            if answers[j] == pattern[i][j]:
                score[i] += 1
    
    # first.append(first[:len(first) % len(answers)])
    
    res = [0]
    max_n = 0
    for i in range(1,4):
        if max_n < score[i]:
            max_n = score[i]
            res[0]=i

        elif res[0] != 0 and max_n == score[i]:
            res.append(i)

    sorting = sorted(res)        

    return sorting