lis = []
while True:
    num = int(input('Digite um valor:'))
    lis.append(num)
    que = input('Gostaria de continuar? [S/N]: ').upper().strip()
    if que == 'S':
        continue
    if que == 'N':
        lis.sort(reverse=True)
        print(f'Programa finalizado com sucesso!!\nA lista final teve um total de {len(lis)} números e ficou assim: {lis}')
        if 5 in lis:
            print(f'O número 5 estava na posição {lis.index(5)+1} da lista!!')
            break
        elif 5 not in lis:
            print('O número 5 não estava na lista!!')
            break