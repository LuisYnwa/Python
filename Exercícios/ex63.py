print('---' * 20)
print('Sequência de Fibonacci')
print('---' * 20)
num = int(input('Quantos termos da sequência de Fibonacci você quer mostrar?: '))
pte = 0
pted = 1
som = 0
cont = 1
while cont <= num:
    print(som, end=' ')
    pte = pted
    pted = som
    som = pte + pted
    cont += 1
print('Fim do programa!!')
