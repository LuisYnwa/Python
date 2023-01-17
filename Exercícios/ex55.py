ma = 0
me = 0
for pe in range(1, 6):
    peso = float(input(f'Insira o peso da {pe}° pessoa: '))
    if pe == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        elif peso < me:
            me = peso 
print(f'O maior peso é da {pe}° pessoa com {ma}')
print(f'O menor peso é da {pe}° pessoa com {me}')