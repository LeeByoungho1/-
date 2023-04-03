def solution(numbers):
    answer = 0
    m1 = numbers[0]
    
    for i in numbers:
        if m1 < i:
            m1 = i
    numbers.remove(m1)
    m2 = numbers[0]
    for i in numbers:
        if m2 < i:
            m2 = i
    answer = m1 * m2
    return answer