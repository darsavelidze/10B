f = open('13.txt')
s = [int(x) for x in f]

for i in range(0, len(s) - 1):
    print(s[i], s[i + 1])


# 0 1 2 3 4
# 2 9 0 7 6