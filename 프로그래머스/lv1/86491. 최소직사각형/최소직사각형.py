def solution(sizes):
    mx1 = max(sizes[0])
    mx2 = min(sizes[0])
    
    for i in sizes:
        if mx1 < max(i):
            mx1 = max(i)
    
    for i in sizes:
        if mx2 < min(i):
            mx2 = min(i)
    answer = mx1 * mx2
    return answer