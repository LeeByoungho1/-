def solution(bin1, bin2):
    answer = ''
    
    a = bin(int(bin1, 2) + int(bin2, 2))
    answer += a
    new_str = answer.replace('0b', '')
    return new_str