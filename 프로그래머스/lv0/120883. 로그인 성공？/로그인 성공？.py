def solution(id_pw, db):
    l = []
    for i in range(len(db)):
        l.append(db[i][0])
    
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in l:
        answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer