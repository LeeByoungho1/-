def solution(array, commands):
    answer = []
    l = array.copy()
    ll = []
    for i in range(len(commands)):
        l = array.copy()
        x = commands[i][0]-1
        y = commands[i][1]
        z = commands[i][2]-1
        ll = array[x:y]
        ll.sort()
        answer.append(ll[z])
    return answer