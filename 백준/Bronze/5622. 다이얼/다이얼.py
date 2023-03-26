import sys
input = sys.stdin.readline

S = list(str(input()))
ans = 0

for element in S:
    if element == 'A' or element == 'B' or element == 'C':
        ans += 3
    elif element == 'D' or element == 'E' or element == 'F':
        ans += 4
    elif element == 'G' or element == 'H' or element == 'I':
        ans += 5
    elif element == 'J' or element == 'K' or element == 'L':
        ans += 6
    elif element == 'M' or element == 'N' or element == 'O':
        ans += 7
    elif element == 'P' or element == 'Q' or element == 'R' or element == 'S':
        ans += 8
    elif element == 'T' or element == 'U' or element == 'V':
        ans += 9
    elif element == 'W' or element == 'X' or element == 'Y' or element == 'Z':
        ans += 10
    
print(ans)