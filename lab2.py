bolfi = list()
while True:
    name = str(input('Insira o nome do aluno: '))
    scor1 = float(input('Insira a 1° nota do aluno: '))
    scor2 = float(input('Insira a 2° nota do aluno: '))
    ave = (scor1 + scor2) / 2
    bolfi.append([name, [scor1, scor2], ave])
    ask = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()
    if ask == 'N':
        break
#for n, sc in enumerate(bolfi):
for n in len(bolfi[0]):
    [print('NOME:', i,) for i, in zip(bolfi[0], )]
    [print(': MÉDIA', j) for j, in zip(bolfi[1])]

#': MÉDIA', k