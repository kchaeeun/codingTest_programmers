def solution(a, b):
    answer = ''
    dic = {1:0, 2: -2, 3: 0, 4:-1, 5:0, 6:-1, 7:0, 8:0, 9:-1, 10:0, 11:-1, 12:0}
    date = (a-1) * 31 + b
    for i in range(1,a):
        date += dic[i]
        
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    answer = day[(date % 7)-1]
    
    return answer