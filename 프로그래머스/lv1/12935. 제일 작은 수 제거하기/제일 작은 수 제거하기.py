def solution(arr):
    l = arr.copy()
    l.sort()
    arr.remove(l[0])
    if len(arr) == 0:
        arr = [-1]
    return arr