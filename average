conjunto = (10, 7, 3, 1, 8, 9, 11)
l = []


def mediaConjunto(all_numbers):
    sum = 0
    cont = 0
    for c in conjunto:
        sum += c
        cont += 1

    mean = sum / cont
    for c in conjunto:
        if c < mean:
            l.append(c)

    print(f'The numbers {l} are less that mean of set')


mediaConjunto(conjunto)
