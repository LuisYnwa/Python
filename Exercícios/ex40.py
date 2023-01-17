n1 = float(input('Insira a nota do primeiro aluno: '))
n2 = float(input('Insira a nota do segundo aluno: '))
n3 = float(input('Insira a nota do terceiro aluno: '))
med = (n1+n2+n3) / 3
if med <= 5.0: 
    print ('Reprovado!')
elif med >=5.0 and med < 7.0:
    print ('Vai ficar de recuperação hein!!')
else:
    print ('Aprovado!!')