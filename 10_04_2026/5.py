for i in range(4, 100):
    N = bin(i)[2:]
    if i % 3 == 0:
        N = N + N[-3:]
    else:
        o = i % 3 * 3
        k = bin(o)[2:]
        N = N + k
    R = int(N, 2)
    if R >= 200:
        print(i, R)

