def solution(citations):
    answer = 0
    citations.sort(reverse=True)        # [6,5,3,1,0] # [2,3,5,6,9,10,11]
    for c in range(len(citations)):
        if c+1 <= citations[c]:
            answer = c+1
    
    return answer