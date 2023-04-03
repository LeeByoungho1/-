def solution(num_list):
    answer = []
    index_0 = 0
    index_1 = 0
    for i in num_list:
        if i % 2 == 0:
            index_0 += 1
        else:
            index_1 += 1
    answer.append(index_0)
    answer.append(index_1)
    return answer