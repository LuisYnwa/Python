x = float(input('Insira o comprimento da primeira reta: '))
y = float(input('Insira o comprimento da segunda reta: '))
z = float(input('Insira o comprimento da terceira reta (base):'))
if x + y == z:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')