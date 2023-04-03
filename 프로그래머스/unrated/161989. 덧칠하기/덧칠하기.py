def solution(n, m, section):
    answer = 0
    b = ['O'] * n
    for i in section:
        b[i-1] = 'X'
    while 'X' in b:
        for i in range(len(b)):
            if b[i] == 'X':
                b[i:i+m] = ['O']*m
                answer += 1
    return answer