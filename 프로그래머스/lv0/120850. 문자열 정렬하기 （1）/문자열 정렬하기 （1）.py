import re
def solution(my_string):
    answer = []
    numbers = list(re.sub(r'[^0-9]', '', my_string))
    for i in numbers:
        answer.append(int(i))
    answer.sort()
    return answer