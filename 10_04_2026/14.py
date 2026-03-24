import string

alf = '0123456789' + string.ascii_uppercase[:19]

for x in alf:
    a1 = '923' + x + '874'
    b1 = '524' + x + '6152'
    a = int(a1, 29)
    b = int(b1, 29)
    c =a + b
    if c % 28 == 0:
        print(c // 28)