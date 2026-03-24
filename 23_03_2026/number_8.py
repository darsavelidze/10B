f = open('8.csv')

count = 0
for line in f:
    s = [int(x) for x in line.split(';')]
    s = sorted(s)
    cond_1 = s[3] > (s[0] + s[1] + s[2])
    cond_2 = len(set(s)) == len(s)
    if cond_1 and cond_2:
        count += 1

print(count)
