def count_sets(num):
    counts = [0] * 10
    for digit in num:
        if digit == '9':
            counts[6] += 1
        else:
            counts[int(digit)] += 1

    if counts[6] % 2 == 0:
        counts[6] = counts[6] // 2
    else:
        counts[6] = (counts[6] + 1) // 2

    max_count = max(counts)
    if max_count > 0:
        set_count = max_count

    return set_count

num = input()
print(count_sets(num))
