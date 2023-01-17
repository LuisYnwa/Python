print ('Digite [1] para bases binárias\n[2] para bases octais\nou [3] para bases hexadecimais')
num = int(input('Escolha para que base você irá converter: '))
conv = int(input('Insira o valor para conversão: '))
if num == 1:
    print (f'Em binário esse valor é: {conv:b}') 
elif num == 2:
    print (f'Em octal esse valor é: {conv:o}')
elif num == 3:
    print(f'Em hexadecimal esse valor é: {conv:X}')
else:
    print('Tu digitou um número diferente burrão')
    
# :b para binário, :o octal, :x hexadecimal com letras minúsculas e :X para hexadecimal com letras maiúsculas