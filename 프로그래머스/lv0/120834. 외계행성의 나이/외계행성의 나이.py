def solution(age):
    answer = ''
    for i in str(age):
        if i == '0':
            answer += 'a'
        elif i == '1':
            answer += 'b'
        elif i == '2':
            answer += 'c'
        elif i == '3':
            answer += 'd'
        elif i == '4':
            answer += 'e'
        elif i == '5':
            answer += 'f'
        elif i == '6':
            answer += 'g'
        elif i == '7':
            answer += 'h'
        elif i == '8':
            answer += 'i'
        else:
            answer += 'j'
    return answer