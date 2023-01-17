n = int(input('Insira um número para transformá-lo em fatorial: '))
co = n
f = 1
if n < 0:
    print('Não é possível fazer a fatorial de um número negativo!!')
elif n == 0:
    print('O fatorial de 0 é 1')
else:
    while co >= 1:
        print(f'{co}', end= '')
        print(' x ', end='')
        f *= co
        co -= 1
    print(f' O número fatorial é: {f}')
