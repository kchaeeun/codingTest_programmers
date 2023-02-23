def solution(array, commands):
    answer = []
    before = []
    after = []
    
    for i in commands:
        before.append(array[i[0]-1:i[1]])
   
    for i in before:
        # sort 시 append 안됨
        sorting = sorted(i)
        after.append(sorting)
        
    for i in range(len(commands)):
            answer.append(after[i][commands[i][2]-1])
    
    return answer
