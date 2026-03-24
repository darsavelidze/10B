min_z = 100000000000
for x in range(1, 2030):
    r = 6 ** 2030 + 6 ** 100 - x
    k = 0
    while r > 0:
        if r % 6 == 0:
            k += 1
        r //= 6

    if k < min_z:
        min_z = k

print(min_z)

