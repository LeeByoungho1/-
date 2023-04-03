def solution(array):
    answer = 0
    l = []
    for i in array:
        l = l + list(map(int,str(i)))
    print(l)
    for i in l:
        if i == 7:
            answer += 1
    return answer