val = float(input('Insira o valor do produto R$: '))
cond = int(input('Essas são as opções de pagamento:\n[1] para pagamentos à vista\n[2] á vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nInsira a condição de pagamento: '))
vis = val - (val * 0.10)
visc = val - (val * 0.05)
car3x = float(val + (val * 0.20))
if cond == 1:
    print(f'Você ganhou um desconto de 10%!\nO valor final a pagar é: R${vis:.5}')
elif cond == 2:
    print(f'Você ganhou um desconto de 5%!\nO valor final a pagar é: R${visc:.5}')
elif cond == 3:
    print(f'Você pagará o valor normal de R${val:.5} em 2x no cartão sem juros.')
elif cond == 4:
    vez = int(input('Insira em quantas vezes deseja parcelar o produto (até 12x): '))
    parc = float(car3x / vez)
    print(f'Você pagará o produto em {vez} vezes com parcelas de R${parc:.5}, totalizando o valor de R${car3x:.5} .')
else:
    print('Você não digitou uma opção válida!!')
