from random import shuffle
nam1 = str (input('Digite o nome do primeiro aluno:'))
nam2 = str (input('Digite o nome do segundo aluno: '))
nam3 = str (input('Digite o nome do terceiro aluno: '))
nam4 = str (input('Digite o nome do quarto aluno: '))
list = [nam1, nam2, nam3, nam4]
shuffle (list)
print (f'A lista de quem vai apagar o quadro é:{list}') 