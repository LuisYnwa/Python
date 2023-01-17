#quebrado
s = 0
cou = 0
for i in range(1, 7):
    int(input('Insira o número inteiro: '))
    if i % 2 == 0:
        cou = cou + 1
        s = s + i
print(f'Você informou {cou} números pares e a soma entre eles foi de: {s}')


