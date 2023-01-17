nomtemp = list()
pessoas = list()
pesos = list()
pleves = list()
psadas = list()
while True:
    nome = str(input('Digite o nome da pessoa: '))
    nomtemp.append(nome)
    peso = int(input('Digite agora o peso: '))
    nomtemp.append(peso)
    pessoas.append(nomtemp[:])
    nomtemp.clear()
    con = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if con == 'N':
        break
print(f'Ao todo {len(pessoas)} pessoas foram cadastradas!!')
#print(pessoas)
for pesin in pessoas:
    pesos.append(pesin[1])
#print(pesos)
for pe in pessoas:
    if pe[1] >= max(pesos): #aqui ele conta e analisa se o segundo valor (número) de cada lista dentro da lista é maior ou igual ao maior valor da lista dedicada apenas aos pesos
        psadas.append(pe[0]) #se for, ele appende o valor que está do lado desse número (nome, na posição 0) na sublista da contagem atual por conta de ter várias delas uma dentro da outra
    elif pe[1] <= min(pesos):
        pleves.append(pe[0])
print(f'O maior pesso foi de {psadas} com {max(pesos)} kg e o menor foi de {pleves} com {min(pesos)} kg')
    
