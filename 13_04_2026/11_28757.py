from math import *

K = 289
N = 1015 + 10
i = ceil(log2(N))
I = ceil(K * i / 8)
print(I)
print(I * 524288 / 1024 / 1024)
