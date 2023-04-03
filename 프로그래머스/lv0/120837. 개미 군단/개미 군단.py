def solution(hp):
    
    jang = hp // 5 
    hp = hp - 5 * jang
    boung = hp // 3
    hp = hp - 3 * boung
    answer = jang + boung + hp
    return answer