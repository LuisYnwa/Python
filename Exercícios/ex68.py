from random import randint 
print('---' * 20)
print('JOGO DE PAR OU ÍMPAR')
print('---' * 20)
cont = 0
nu = int(input('Por favor, insira seu número para disputar com o computador: '))
pp = str(input('Ímpar ou par? [I/P]: ')).upper().strip()
while True:
    pc = randint (1, 10)
    resu = pc + nu
    ref = resu % 2
    if ref == 0 and pp == 'P' or ref != 0 and pp == 'I':
        print(f'Você ganhou!! Você jogou {nu} e o computador jogou {pc}, totalizando {resu}')
        cont += 1
    else:
        print(f'Você perdeu após {cont} tentativas, não desista!!')
        print(f'Você jogou {nu} e o computador jogou {pc}, totalizando {resu}')
        break
    nu = int(input('Vamos para mais uma rodada!! Insira um novo número: '))
    pp = str(input('Ímpar ou par? [I/P]: ')).upper().strip()