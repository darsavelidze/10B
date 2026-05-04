alf = '0123456789AB'
for x in alf:
    a = int('154' + x + '3', 12)
    b = int('1' + x + '365', 12)
    c = a + b
    if c % 13 == 0:
        print(c // 13)
