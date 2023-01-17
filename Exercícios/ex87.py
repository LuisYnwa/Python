calcu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = tcolunas = 0
for li in range(0, 3):
    for colu in range(0, 3):
        calcu [li] [colu]= int(input(f'Digite o valor de [{li}, {colu}]:'))
print(f'Matriz:')
for li in range(0, 3):
    for colu in range(0, 3):
        print(f'[{calcu[li] [colu]:^5}]', end='')#:^5 representa cinco casas decimais e o chapeuzinho é a centralização dele no bloco
        if calcu [li] [colu] % 2 == 0:
            pares += calcu [li] [colu]
        if colu == 2:
            tcolunas += calcu [li] [colu]
    print()
print(f'A soma dos números pares é de: {pares}')
print(f'A soma dos valores da 3° coluna é de: {tcolunas}')
print(f'O maior valor da segunda linha é {max(calcu[1])}')