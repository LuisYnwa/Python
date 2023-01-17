matri = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contum = 0
contdo = 0
for p in range (0,3):
    for i in range (0, 3):
        valo = int(input(f'Digite o valor para [{contum} , {contdo}]: '))
        if contum == contdo:
            matri[0].append(valo)
            contdo += 1
        elif contum < contdo:
            if contdo == 2:
                matri[2].append(valo)
                contum += 1
                contdo = 0
            else:
                matri[1].append(valo)
                contdo += 1
        elif contum > contdo:
            matri[2].append(valo)
            contdo += 1
print('=='*20)
print('Resultado final da matriz:')
print(matri)

