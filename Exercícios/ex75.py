val1 = float(input(f'Insira o 1° valor:'))
val2 = float(input(f'Insira o 2° valor:'))
val3 = float(input(f'Insira o 3° valor:'))
val4 = float(input(f'Insira o 4° valor:'))
valos = (val1, val2, val3, val4)
print(f'A tupla de valores foi: {valos}')
if 9 in valos:
    print(f'O número nove apareceu {valos.count(9)} vezes')
if 3 in valos:
    print(f'O número três foi digitado na {valos.index(3)+1}° posição')
print(f'Os valores pares digitados foram: ', end=' ')
for i in valos:
    if i % 2 == 0:
        print(i, end=' ')