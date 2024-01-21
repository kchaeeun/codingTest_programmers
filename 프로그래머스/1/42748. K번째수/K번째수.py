def solution(array, commands):
    answer = []
    command = []
    for i in commands:  # i = [2,5,3]
        command = sorted(array[i[0]-1:i[1]])
        answer.append(command[i[2]-1])
    return answer