p = float(input('Insira seu peso: '))
a = float(input('Insira sua altura: '))
cal = p / (a**2)
if cal <= 18:
    print(f'Você está abaixo do peso com o IMC de {cal:.4}!')
elif cal >= 18.1 and cal <= 25:
    print(f'Você está no peso ideal com o IMC de {cal:.4}!')
elif cal >= 25.1 and cal <= 30:
    print(f'Você está na faixa de sobrepeso com o IMC de {cal:.4}!')
elif cal >= 30.1 and cal <= 40:
    print(f'Você está na faixa da obesidade com o IMC de {cal:.4}!')
else:
    print(f'Você está na faixa da obesidade móbida com o IMC de {cal:.4}!')