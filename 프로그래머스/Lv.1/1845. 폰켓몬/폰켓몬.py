def solution(nums):
    answer = 0
    only_num = set(nums)       # 중복 제거
    
    if len(only_num) > (len(nums) + 1) // 2:
        answer = (len(nums) + 1) // 2
    else:
        answer = len(only_num)
                
    return answer