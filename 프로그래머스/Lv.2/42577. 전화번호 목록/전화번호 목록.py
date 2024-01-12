def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        idx = len(phone_book[i])
        # for j in range(len(phone_book)):
        # if phone_book[i] != phone_book[i+1]:
        if phone_book[i+1][:idx] == phone_book[i]:
            return False
    return answer