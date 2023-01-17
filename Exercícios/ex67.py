cont = 0
while True:
    num = int(input('Insira o número para ver sua respectiva tabuada: ')) 
    if num < 0:
        print('Não é possível fazer uma tabuada de um número inteiro!!')
        break
    print(f'A tabuada do {num} é:')
    if cont >= 10:
        cont = 0
    while cont <= 9:
        cont += 1
        res = num * cont
        print(f'{num} x {cont} = {res}')
    