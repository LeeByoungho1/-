def solution(n, arr1, arr2):
    
    l1 = []
    for i in arr1:
        l1.append(bin(i)[2:])   
    for i in range(len(l1)):
        if len(l1[i]) < n:
            l1[i] = ('0'*(n-len(l1[i])))+l1[i]
    l2 = []
    for i in arr2:
        l2.append(bin(i)[2:])
    for i in range(len(l2)):
        if len(l2[i]) < n:
            l2[i] = ('0'*(n-len(l2[i])))+l2[i]
    ls1 = []
    for i in l1:
        ll = list(i)
        ssap = ''
        for j in ll:
            if j == '1':
                ssap += '#'
            else:
                ssap += ' '
        ls1.append(ssap)
    ls2 = []
    for i in l2:
        ll = list(i)
        ssap = ''
        for j in ll:
            if j == '1':
                ssap += '#'
            else:
                ssap += ' '
        ls2.append(ssap)    
    answer = []
    for j in range(len(ls1)):
        result = ''
        for i in range(len(ls1[j])):  
            if ls1[j][i] == '#':
                result += '#'
            elif ls2[j][i] == '#':
                result += '#'
            else:
                result += ' '
        answer.append(result)
        
    return answer