c = float(input('Insira o valor da casa R$:'))
s = float(input('Insira seu salário R$: '))
a = int(input('Em quantos anos irá pagar? R$: '))
pres = c / (a*12)
sal = (s * 30) / 100
if sal >= pres:
    print(f'Crédito aprovado! Você pagará R${pres:.5} de prestação durante {a} anos')
else:
    print (f'Crédito reprovado! \nA prestação seria de {pres:.5} porém seu salário é de apenas {s}, necessitando de um valor igual a 30 por cento dele para aprovação ')