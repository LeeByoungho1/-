def solution(a, b):
    answer = ''
    if a in [1,4,7]:
        if b % 7 == 1:
            answer = 'FRI'
        elif b % 7 == 2:
            answer = 'SAT'
        elif b % 7 == 3:
            answer = 'SUN'
        elif b % 7 == 4:
            answer = 'MON'
        elif b % 7 == 5:
            answer = 'TUE'
        elif b % 7 == 6:
            answer = 'WED'
        elif b % 7 == 0:
            answer = 'THU'
            
    elif a in [2,8]:
        if b % 7 == 1:
            answer = 'MON'
        elif b % 7 == 2:
            answer = 'TUE'
        elif b % 7 == 3:
            answer = 'WED'
        elif b % 7 == 4:
            answer = 'THU'
        elif b % 7 == 5:
            answer = 'FRI'
        elif b % 7 == 6:
            answer = 'SAT'
        elif b % 7 == 0:
            answer = 'SUN'
            
    elif a in [3,11]:
        if b % 7 == 1:
            answer = 'TUE'
        elif b % 7 == 2:
            answer = 'WED'
        elif b % 7 == 3:
            answer = 'THU'
        elif b % 7 == 4:
            answer = 'FRI'
        elif b % 7 == 5:
            answer = 'SAT'
        elif b % 7 == 6:
            answer = 'SUN'
        elif b % 7 == 0:
            answer = 'MON'
            
    elif a == 5:
        if b % 7 == 1:
            answer = 'SUN'
        elif b % 7 == 2:
            answer = 'MON'
        elif b % 7 == 3:
            answer = 'TUE'
        elif b % 7 == 4:
            answer = 'WED'
        elif b % 7 == 5:
            answer = 'THU'
        elif b % 7 == 6:
            answer = 'FRI'
        elif b % 7 == 0:
            answer = 'SAT'
    
    elif a == 6:
        if b % 7 == 1:
            answer = 'WED'
        elif b % 7 == 2:
            answer = 'THU'
        elif b % 7 == 3:
            answer = 'FRI'
        elif b % 7 == 4:
            answer = 'SAT'
        elif b % 7 == 5:
            answer = 'SUN'
        elif b % 7 == 6:
            answer = 'MON'
        elif b % 7 == 0:
            answer = 'TUE'
    
    elif a in [9,12]:
        if b % 7 == 1:
            answer = 'THU'
        elif b % 7 == 2:
            answer = 'FRI'
        elif b % 7 == 3:
            answer = 'SAT'
        elif b % 7 == 4:
            answer = 'SUN'
        elif b % 7 == 5:
            answer = 'MON'
        elif b % 7 == 6:
            answer = 'TUE'
        elif b % 7 == 0:
            answer = 'WED'
    
    elif a == 10:
        if b % 7 == 1:
            answer = 'SAT'
        elif b % 7 == 2:
            answer = 'SUN'
        elif b % 7 == 3:
            answer = 'MON'
        elif b % 7 == 4:
            answer = 'TUE'
        elif b % 7 == 5:
            answer = 'WED'
        elif b % 7 == 6:
            answer = 'THU'
        elif b % 7 == 0:
            answer = 'FRI'
    return answer