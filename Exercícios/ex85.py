lnums = [[], []]
for i in range (1,7):
    valo = float(input(f'Insira o {i} valor: '))
    if valo % 2 == 0:
        lnums[0].append(valo)
    elif valo % 2 == 1:
        lnums[1].append(valo)
lnums[0].sort()
lnums[1].sort()
print(f'Lista final: {lnums}\nLista de números pares: {lnums[0]}\nLista de números ímpares: {lnums[1]}')
    
