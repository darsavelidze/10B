for i in range(1, 100):
    N = bin(i)[2:]
    if i % 2 == 0:
        N = N + '10'
    else:
        N = '1' + N + '00'
    R = int(N, 2)
    if R > 107:
        print(i, R)
        break