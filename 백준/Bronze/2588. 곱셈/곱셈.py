A = int(input())
B = int(input())

dig100_B = B // 100
dig10_B = (B - (dig100_B * 100)) // 10
dig1_B = (B - (dig100_B * 100) - (dig10_B * 10)) // 1

print(A * dig1_B)
print(A * dig10_B)
print(A * dig100_B)
print(A * B)