x = float(input('Insira o comprimento da primeira reta x: '))
y = float(input('Insira o comprimento da segunda reta y: '))
z = float(input('Insira o comprimento da terceira reta (base) z: '))
if x + y >= z and x + z >= y and z + y >= x:
    print('Essas retas podem formar um triângulo', end=' ' )
    if x == y == z:
        print('Equilátero!')
    elif x != y != z != x:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('Essas retas não podem formar um triângulo :c')

    #if x == y != z or x != y == z or x == z != y