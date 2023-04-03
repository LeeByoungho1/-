def solution(array, n):
    array.sort()
    l = array[::-1]
    answer = l[0]
    num = abs(n-l[0])
    l.remove(l[0])
    for i in l:
        if abs(n-i) < num:
            num = abs(i - n)
            answer = i
        elif abs(i - n) == num:
            answer = i
    return answer