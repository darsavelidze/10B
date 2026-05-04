f = open('13.txt')
data = [int(x) for x in f]

N = min([x for x in data if x % 15 != 0])

s = []

for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a % N == 0 and b % N == 0:
        s.append(a + b)

print(len(s), max(s))
