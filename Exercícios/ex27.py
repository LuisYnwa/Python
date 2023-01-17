nom = str (input('Insira aqui o seu nome completo: '))
first, *middle, last = nom.split()
print(first, last)