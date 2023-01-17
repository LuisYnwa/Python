escr = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numus = int(input('Digite o número que irá ver por inteiro (de 0 a 20): '))
    if numus < 0 or numus > 20:
        print('Número inválido!! Tente novamente')
        continue
    print(f'O número digitado foi {escr[numus]}')
    go = input('Você gostaria de continuar? [S/N]: ').upper().strip()
    if go == 'N':
        print('Programa encerrado!!')
        break