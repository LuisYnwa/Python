from random import randrange 
ran = randrange(1, 6) 
num = int(input('Tente acertar o número de 1 a 5:'))
if num == ran:
    print ('Parabéns! Você acertou o número que o computador pensou!')
else:
    print (f'Poxa, você errou o número que o computador pensou :c, a resposta certa era {ran}')
