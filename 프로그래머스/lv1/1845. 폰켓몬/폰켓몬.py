def solution(nums):
    l = list(set(nums))
    n = int(len(nums) / 2)
    answer = len(l)
    if len(l) >= n:
        answer = n
        
    return answer