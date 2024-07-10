def solution(left, right):
    answer = 0
    cnt_list = []
    idx = 0
    
    for i in range(left, right+1):
        cnt_list.append(i)
        # 약수 구하기 - n로 나눈 나머지가 0인 경우 약수
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            cnt_list[idx] = i
        else: 
            cnt_list[idx] = -i
        idx += 1
        
    return sum(cnt_list) #리스트의 총합  