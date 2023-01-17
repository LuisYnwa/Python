from math import sqrt
print('--'*20)
print('CALCULADORA EM PYTHON')
print('--'*20)
go = 'S'
while go == 'S':
    print('[1] soma (+)\n[2] subtração (-)\n[3] multiplicação (X)\n[4] divisão (/)\n[5] potenciação (²)\n[6] raiz')
    op = int(input('Qual operação você gostaria de realizar?: '))
    if op == 1:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
        r = n1 + n2
        print(f'O resultado final da adição é {r}.')
    elif op == 2:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
        r = n1 - n2
        print(f'O resultado final da subtração é {r}.')
    elif op == 3:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
        r = n1 * n2
        print(f'O resultado final da multiplicação é {r}.')
    elif op == 4:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
        r = n1 / n2
        print(f'O resultado final da divisão é {r}.')
    elif op == 5:
        n1 = int(input('Insira o valor: '))
        n2 = int(input('Elevado a quanto?: '))
        r = n1 ** n2
        print(f'O resultado final da potenciação é {r}.')
    elif op == 6:
        n1 = int(input('Digite o valor do radicando: '))
        ra = sqrt(n1) 
        print(f'O resultado final da raiz quadrada é {ra}.')
    else: 
        print('Comando inválido!! Tente novamente.')
    go = str(input('Gostaria de continuar? [S/N]: ')).upper().strip()
    if go == 'N':
        print('Programa encerrado, obrigado por utilizar!!')
        break