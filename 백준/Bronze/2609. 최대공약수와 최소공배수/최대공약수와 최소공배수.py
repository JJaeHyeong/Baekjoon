x, y = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result

if x > y:
    a, b = y, x
else:
    a, b = x, y

print(gcd(a, b))
print(lcm(a, b))