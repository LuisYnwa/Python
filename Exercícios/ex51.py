t = int(input('Insira o primeiro termo da P.A: '))
r = int(input('Insira a razão da P.A: '))
cal = t + 9 * r
for c in range(t, cal + r, r):
        print(c, end=' > ')
print('ACABOU FINALMENTE!!!!!')