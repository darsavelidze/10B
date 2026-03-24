alf = '0123456'
k = 0
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    w = n1 + n2 + n3 + n4 + n5
                    if n1 != '0':
                        if w.count('0') == 1 and w.count('1') <= 2:
                            k += 1

print(k)