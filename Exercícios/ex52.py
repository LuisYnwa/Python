n = int(input('Insira um número inteiro: '))
for p in range(1, n+1):
        print(p, end=' ')
if n % 3 > 0:
    print('\nEle é primo')
else:
    print('\nEle não é primo')
            