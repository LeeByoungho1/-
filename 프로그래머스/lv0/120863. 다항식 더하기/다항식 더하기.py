def solution(polynomial):
    l = polynomial.split(" ")
    for i in range((len(l)//2)):
        l.remove("+")
        
    x = []
    n = []
    for i in l:
        if 'x' in i:
            if i == 'x':
                x.append('1x')
            else:
                x.append(i)
        else:
            n.append(i)
            
    xx = []
    for i in x:
        xx.append(i.split("x")[0])
    
    a = 0
    for i in xx:
        a += int(i)
    
    b = 0
    for i in n:
        b += int(i)
    
    
    if b == 0:
        if a == 1:
            answer = "x"
        else:
            answer = f"{a}x"
    elif a == 0:
        answer = f"{b}"
    elif a == 1:
        answer = f"x + {b}"
    else:
        answer = f"{a}x + {b}"
    
    return answer