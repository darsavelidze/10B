s = 'АВЕНС'
k = 1
for n1 in s:
    for n2 in s:
        for n3 in s:
            for n4 in s:
                w = n1 + n2 + n3 + n4
                if w.count('Е') == 0 and w.count('АА') == 0:
                    print(k, w)
                k += 1


