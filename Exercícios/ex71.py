print('=='*20)
print('Bem-vindo ao caixa eletrônico do banco MULTIFINANCE!')
print('=='*20)
val = int(input('Quanto você gostaria de sacar? R$:'))
cedul = val//200
rest = val%200
if cedul > 0:
    print(f"Total de {cedul} notas de R$200")
cedul = rest//100
rest %= 100
if cedul > 0:
    print(f"Total de {cedul} notas de R$100")
cedul = rest//50
rest %= 50
if cedul > 0:
    print(f'Total de {cedul} notas de R$50')
cedul = rest//20
rest %= 20
if cedul > 0:
    print(f'Total de {cedul} notas de R$20')
cedul = rest//10
rest %= 10
if cedul > 0:
    print(f'Total de {cedul} notas de R$10')
cedul = rest // 5
rest %= 5
if cedul > 0:
    print(f'Total de {cedul} notas de R$5')
cedul = rest 
if cedul > 0 :
    print(f'Total de {cedul} moedas de R$1')
print('Obrigado por usar nosso caixa! Volte sempre!!')
        