vel = float(input('Insira a velocidade do carro: '))
if vel > 80:
    mul = (vel-80)*7
    print (f'Você ultrapassou o limite e sua multa será de R${mul}')
print ('Você não tem débitos a pagar!')