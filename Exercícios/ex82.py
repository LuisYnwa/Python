lis = []
lisp = []
lisim = []
while True:
    n = int(input('Insira um valor: '))
    lis.append(n)
    if n % 2 == 0:
        lisp.append(n)
    if n % 2 != 0:
        lisim.append(n)
    q = input('Gostaria de continuar? [S/N]: ').upper().strip()
    if q == 'S':
        continue
    elif q == 'N':
        print(f'Programa finalizado!!\n1° lista: {lis}\n2° lista com números pares: {lisp}\n3° lista apenas com números ímpares: {lisim}')
        break
