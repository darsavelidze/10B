N = int(input())
m = float("inf")
for i in range(N):
    x = int(input())
    if x < m:
        m = x


print(m)