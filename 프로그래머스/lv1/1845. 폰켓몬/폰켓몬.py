def solution(nums):
    answer = 0
    get_po = len(nums) // 2
    
    nums=set(nums)
    if get_po < len(nums):
        answer = get_po
    else:    
        answer = len(nums)

    return answer