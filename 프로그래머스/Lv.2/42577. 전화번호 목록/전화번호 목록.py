def solution(phone_book):
    answer = True
    phone_book.sort()       # 정렬해서 for문을 적게 사용하고, 최소로 돌게 한다
    for i in range(len(phone_book)-1):
        idx = len(phone_book[i])
        # for j in range(len(phone_book)):
        # if phone_book[i] != phone_book[i+1]:
        if phone_book[i+1][:idx] == phone_book[i]:
            return False
    return answer