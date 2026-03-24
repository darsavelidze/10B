alf = 'АЕЛПРЬ'
k = 1
for n1 in alf:
    for n2 in alf:
        for n3 in alf:
            for n4 in alf:
                for n5 in alf:
                    w = n1 + n2 + n3 + n4 + n5
                    if n1 not in 'ЬР' and w.count('Л') >= 2:
                        if k % 2 == 0:
                            print(k)
                    k += 1