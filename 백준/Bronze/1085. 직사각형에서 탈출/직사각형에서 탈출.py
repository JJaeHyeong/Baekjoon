x, y, w, h = map(int, input().split())
diff_x = w - x
diff_y = h - y
temp = []
temp.append(x)
temp.append(y)
temp.append(diff_x)
temp.append(diff_y)

print(min(temp))