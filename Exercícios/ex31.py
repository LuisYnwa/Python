viag = float(input('Insira a distância da viagem:'))
if viag <= 200:
    pre = viag*0.50
    print(f'O preço da sua viagem será de: R${pre}')
elif viag > 200:
    pre2 = viag*0.45
    print(f'O preço da sua viagem será de: R${pre2}')
