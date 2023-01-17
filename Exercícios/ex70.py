cont = contpro = contsom = bara = bar = 0
barp = ''
while True:
    cont += 1
    pro = str(input(f'Por favor, informe o nome do {cont}° produto: ')).upper().strip()
    cus = float(input('Quanto ele custou (coloque ponto) ? R$:'))
    contsom += cus
    if cus >= 1000:
        contpro += 1
    if cont == 1 or cus < bara:
        bara = cus
        bar = cus
        barp = pro
    gos = str(input('Você gostaria de continuar? [S/N]: ')) 
    if gos == 'N':
        print(f'Obrigado por participar!!\nA soma total dos seus produtos foi de R${contsom}\n{contpro} produtos custaram mais de R$1000,00\no produto mais barato foi o {barp} que custou R${bara}!!')
        break