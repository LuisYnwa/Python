t = int(input('insira o primeiro termo da P.A: '))
r = int(input('Agora insira a razão: '))
#fo = t + 9 * r (não precisei usar)
co = 1
while co <= 10:
    print(t , end=' > ')
    t = t + r
    co += 1
print('ACABOOUUU!!')