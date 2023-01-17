nu = []
for n in range (1, 6):
    mu = int(input(f'Insira o {n}° valor: '))
    nu.append(mu)
print(nu)
print(f'O maior número digitado foi {max(nu)} na posição {nu.index(max(nu))+1} o menor foi {min(nu)} na posição {nu.index(min(nu))+1}')
