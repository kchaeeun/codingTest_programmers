def solution(numbers):
    answer = ''
    
    # 정수를 문자열로 변경
    numbers = [str(number) for number in numbers]
    
    # 정수를 연이어 붙여서 4자리 수로 만든 후 정렬(numbers의 원소 최대 3자리 수임)
    numbers = sorted(numbers, key = lambda num : (num*4)[:4], reverse=True) # 문자열끼리 곱셈 가능, key는 정렬의 기준값
    
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
        
    return answer