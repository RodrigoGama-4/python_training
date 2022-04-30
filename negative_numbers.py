conjunto = (8, 9, - 2, -18, 10, 1, 0, -5, -9, -11)


def numerosNegativos(all_numbers):
    cont = 0
    for n in all_numbers:
        if n < 0:
            cont += 1
    print(f'No conjunto há {cont} números negativos')


numerosNegativos(conjunto)
