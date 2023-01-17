fra = str(input('Insira a frase/palavra (sem acentos): ')).strip().upper()
pal = fra.split()
jun = ''.join(pal)
inv = ''
for L in range(len(jun) -1, -1, -1):
    inv += jun[L]
print(f'A frase/palavra inserida é: {jun}')
print(f'E seu formato inverso é: {inv}')
if inv == fra:
    print('Ele é um palíndromo!')
else:
    print('Ele não é um palíndromo..')
