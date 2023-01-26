def solution(survey, choices):
    answer = ''
    choice = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            choice[survey[i][1]] += choices[i]%4
        elif choices[i] < 4:
            if choices[i] == 1:
                choice[survey[i][0]] += 3
            elif choices[i] == 2:
                choice[survey[i][0]] += 2
            else:
                choice[survey[i][0]] += 1
                
        elif choices[i] == 4:
            continue
    
    if choice['R'] > choice['T']:
        answer += 'R'
    elif choice['R'] < choice['T']:
        answer += 'T'
    else:
        if ord('T') > ord('R'):
            answer += 'R'
        else:
            answer += 'T'
    
    if choice['C'] > choice['F']:
        answer += 'C'
    elif choice['C'] < choice['F']:
        answer += 'F'
    else:
        if ord('C') > ord('F'):
            answer += 'F'
        else:
            answer += 'C'

    if choice['J'] > choice['M']:
        answer += 'J'
    elif choice['J'] < choice['M']:
        answer += 'M'
    else:
        if ord('J') > ord('M'):
            answer += 'M'
        else:
            answer += 'J'

    if choice['A'] > choice['N']:
        answer += 'A'
    elif choice['A'] < choice['N']:
        answer += 'N'
    else:
        if ord('A') > ord('N'):
            answer += 'N'
        else:
            answer += 'A'

    return answer