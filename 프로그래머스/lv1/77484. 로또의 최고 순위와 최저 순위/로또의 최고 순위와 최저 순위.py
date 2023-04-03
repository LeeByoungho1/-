def solution(lottos, win_nums):
    answer = []
    n = 0
    l = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            n += 1
    for i in range(2):
        if n == 6:
            answer.append(1)
        elif n == 5:
            answer.append(2)
        elif n == 4:
            answer.append(3)
        elif n == 3:
            answer.append(4)
        elif n == 2:
            answer.append(5)
        else:
            answer.append(6)
        n += l
    answer.sort()
    return answer