from math import *

for N in range(1, 1000):
    i = ceil(log2(N))
    K = 2468
    I = K * i
    I = ceil(I / 8)
    if I * 4_635_815 >= 10 * 1024 * 1024 * 1024:
        print(N)