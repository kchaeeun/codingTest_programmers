def solution(sizes):
    # 가로를 세로로 바꿀 수 있음
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        if h > w:
            h, w = w, h
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    return max_w * max_h