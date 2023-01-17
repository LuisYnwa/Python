obj = ('Lápis', 1.80, 'Borracha', 1.35, 'Caderno', 15.60,'Estojo', 6.75, 'Transferidor',  2.00, 'Régua', 3.00, 'Lapiseira', 2.50, 'Mochila', 120.00, 'Caneta', 1.50, 'Apostila', 73.00)
for po in range (0, len(obj)):
    if po % 2 == 0:
        print(f'{obj[po]:.<40}', end='')
    else:
        print(f'R$ {obj[po]:>4.2f}')