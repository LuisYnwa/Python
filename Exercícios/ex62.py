#quebrado no final
t = int(input('insira o primeiro termo da P.A: '))
r = int(input('Agora insira a razão: '))
con = 1
tot = 0
ma = 10
print('A sequência é: ', end='')
while con < 10:
    print(t, end=' > ')
    t = t + r
    con += 1
print('FINISHED')
mt = str(input('Você gostaria de mais termos [S/N]? '))
if mt == 'N':
    print('Então fim do programa!! :)')
elif mt == 'S':
    sm = int(input('Quantos termos a mais?: '))
    while ma != 0:
        sm += ma
        while con == sm :
            print(tot, end=' > ' )
            t += r
            con += 1
print('FIM DESSA DESGRAÇAAAA')

        

