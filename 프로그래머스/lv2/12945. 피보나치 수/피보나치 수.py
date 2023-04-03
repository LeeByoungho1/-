def solution(n):
    n1 = 1
    n2 = 1
    n3 = 2
    
    i = 3
    while i < n:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        i += 1
  
    if n == 2:
        answer = 1
    elif n == 3:
        answer = 2
    else:
        answer = n3 % 1234567
    return answer