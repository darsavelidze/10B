s = '1234567890'
evens = []
for x in s:
    num = int(x)
    if num % 2 == 0:
        evens.append(num)

print(evens)

r = [int(x) for x in s if int(x) % 2 == 0]
print(r)
