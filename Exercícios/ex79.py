lis = []
while True:
    va = int(input('Digite o valor: '))
    if va not in lis:
        lis.append(va)
        print('Valor adicionado com sucesso!!')
    elif va in lis:
        print('O valor já está no sistema!! Por favor insira outro.')
    que = input('Quer continuar? [S/N]: ').upper().strip()
    if que == 'N':
        lis.sort()
        print(f'A lista ficou com os números: {lis}')
        print('Programa finalizado!!')
        break
    elif que == 'S':
        continue
