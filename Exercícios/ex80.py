li = []
for ai in range (0, 6):
    v = int(input(f'Insira o {ai + 1} valor: '))
    if ai == 0 or v > li[-1]:
        li.append(v)
    else: 
        pos = 0
        while pos < len(li):
            if v <= li[pos]:
                li.insert(pos, v)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(li)