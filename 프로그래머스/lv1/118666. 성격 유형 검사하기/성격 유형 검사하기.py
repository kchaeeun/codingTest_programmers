def solution(survey, choices):
    answer = ''
    choice = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            choice[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            choice[survey[i][0]] += 4 - choices[i]
        else:
            continue
    
    if choice['R'] >= choice['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if choice['C'] >= choice['F']:      #c가 f보다 우선인 것은 알고 있음
        answer += 'C'
    else:
        answer += 'F'

    if choice['J'] >= choice['M']:
        answer += 'J'
    else:
        answer += 'M'

    if choice['A'] >= choice['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer