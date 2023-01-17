import random as rn
nom1 = input('Insira aqui o primeiro nome: ')
nom2 = input('Insira aqui o segundo nome: ')
nom3 = input('Insira aqui o terceiro nome: ')
nom4 = input('Insira aqui o quarto nome: ')
rand = [nom1, nom2, nom3, nom4]
sample = rn.sample (rand, len(rand))
print (f'A ordem dos alunos que irão apagar o quadro é: {sample}')
