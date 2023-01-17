print('---------BOLETIM ESCOLAR---------')
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
print('--' * 20)
print('N°   NOME   MÉDIA')
print('--' * 20)
for pos, alun in enumerate(bolfi):
    print(pos, f'{alun[0]:<15}', alun[2])
while True:
    print('--'*20)
    alu = int(input('Mostrar notas de qual aluno?: (use números e insira 999 para parar)'))
    if alu == 999:
        print('Programa finalizado COM SUCESSO!!')
        break 
    elif alu <= len(bolfi) - 1:
        print(f'As notas do aluno(a) {bolfi[alu] [0]} foram: {bolfi[alu] [1]}') # aqui ela procura o aluno de acordo com a variável (alu) pelo número que a alu deu, após isso ela vai selecionar dentro da sublista de notas (1) (que contém as duas notas) e pegar cada uma de acordo com o número entre colchetes acima (0 e 1)
