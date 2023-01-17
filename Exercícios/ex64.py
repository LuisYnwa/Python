cont = 0
som = 0
usu = 0
usu = int(input(f'Insira o {cont + 1}° número inteiro (digite 999 para parar):'))
while usu != 999:
    som += usu
    cont += 1
    usu = int(input(f'Insira o {cont + 1}° número inteiro (digite 999 para parar):'))
print(f'Foram digitados ao todo {cont} números com o somatório total de {som} entre eles')
print('*Desconsiderando o 999')