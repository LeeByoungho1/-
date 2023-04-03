def solution(my_str, n):
    answer = []
    num = 0
    if len(my_str) % n == 0:
        num = len(my_str) // n
    else:
        num = len(my_str) // n + 1
    for i in range(num):
        answer.append(my_str[:n])
        my_str = my_str[n:]
    
    return answer