def solution(angle):
    if angle > 0 and angle < 90:
        ans = 1
    elif angle == 90:
        ans = 2
    elif angle > 90 and angle < 180:
        ans = 3
    elif angle == 180:
        ans = 4
    return(ans)