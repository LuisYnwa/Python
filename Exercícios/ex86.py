matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for li in range(0, 3):
    for co in range(0, 3):
        matriz [li][co] = int(input(f'insira o valor de [{li}, {co}]: ')) 
for li in range(0, 3):
    for co in range(0,3):
        print(f'[{matriz[li] [co]:^5}]', end='') #:^5 representa cinco casas decimais e o chapeuzinho é a centralização dele no bloco
    print()
