for n in range(1, 1000):
    s = '5' + '8' * n
    while '58' in s or '888' in s or '333' in s:
        s = s.replace('58', '5', 1)
        if '333' in s:
            s = s.replace('333', '8', 1)
        else:
            s = s.replace('888', '3', 1)

    r = s.count('3') * 3 + s.count('5') * 5 + s.count('8') * 8
    print('n =', n, 'r =', r)
