re = 'S'
som = cont = ma = me = 0
while re == 'S':
    num = float(input('Digite um número: '))
    re = input('Quer continuar? [S/N]: ').upper().strip()
    cont += 1
    som += num 
    if cont == 1:
        ma = me = num
    else:
        if num > ma:
            ma = num
        elif me < num:
            me = num
med = som / cont
print('Programa finalizado!!')
print(f'Você digitou ao todo {cont} valores e a média entre eles foi de {med}')
print(f'O maior valor foi {ma} e o menor foi {me}')