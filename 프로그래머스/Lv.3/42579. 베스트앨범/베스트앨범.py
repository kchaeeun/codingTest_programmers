def solution(genres, plays):
    answer = []
    dic_sum = {}
    
    for i in range(len(plays)):
        dic_sum[genres[i]] = 0
    for i in range(len(plays)):
        dic_sum[genres[i]] += plays[i]
        
    dic_sum = dict(sorted(dic_sum.items(), key = lambda item:item[1], reverse=True))
    for i in dic_sum:
        dic_sum[i] = []
        
    for i in range(len(plays)):
        dic_sum[genres[i]].append((i, plays[i]))  # Store (index, play) pairs for each genre
    
    for i in dic_sum:
        dic_sum[i].sort(key=lambda x: (x[1], -x[0]), reverse=True)  # Sort by play count and then index
        answer.append(dic_sum[i][0][0])
        if len(dic_sum[i]) > 1:
            answer.append(dic_sum[i][1][0])
        
    return answer