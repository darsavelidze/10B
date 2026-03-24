z = 0
for i in range(100, 1000):
    x = i
    k = 0
    while x > 0:
        if x % 6 == 5:
            k += 1
        x = x // 6

    if k >= 2:
        z += 1

print(z)