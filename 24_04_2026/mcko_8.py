p = 5
q = 7
e = 11
for d in range(1, 40):
    f_n = (p - 1) * (q - 1)
    r = (d * e) % f_n
    if r == 1:
        print(d)


