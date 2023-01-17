sal = float(input('Insira quanto você ganha R$: '))
if sal > 1.250:
    sal2 = sal * 1.10 
elif sal < 1.250:
    sal2 = sal * 1.15 
print(f'O seu novo salário será de R${sal2:.2f}')