def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0,numbers[-1])
        numbers.pop()
    else:
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
    return numbers