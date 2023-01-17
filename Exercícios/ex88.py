from random import randint
from time import sleep
print('~~' * 20)
print(f'               MEGA-SENA')
print('~~' * 20)
vez = int(input('Quantas apostas deseja realizar?: '))
print('SORTEANDO...', end='')
for i in range(0, 4):
    print('.', end='')
    sleep(1)
for me in range(0, vez):
    jogadas = []
    while len(jogadas) <= 6:
        nume = randint(1, 60)
        if nume not in jogadas:
            jogadas.append(nume)
    jogadas.sort()
    print(f'\nJogo {me + 1}: {jogadas}')
print('---------BOA SORTE!!!!---------')