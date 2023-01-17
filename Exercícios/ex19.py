from random import choice
nom1 = input('Insira o nome do primeiro aluno: ')
nom2 = input('Insira o nome do segundo aluno: ')
nom3 = input('Insira o nome do terceiro aluno: ')
nom4 = input('Insira o nome do quarto aluno: ')
ran = [nom1, nom2, nom3, nom4]
print (f'O aluno escolhido para apagar o quadro foi o {choice(ran)}')
