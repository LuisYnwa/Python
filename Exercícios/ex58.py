from random import randrange 
ran = randrange (1, 10)
nu = int(input('Tente acertar o número que o computador pensou:'))
cont = 1
while nu != ran:
    nu = int(input('Você errou! Tente outro número: '))
    cont += 1
print(f'Você acertou! O número do computador era {ran} e você tentou {cont} vezes!')