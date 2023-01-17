#programa simulando uma calculadora de juros compostos para um cliente de um banco fictício
import time
go = 'S'
ju = 0
print('--'*10)
print('Olá! Seja bem-vindo ao banco MULTIFINANCE!')
print('--'*10)
while go == 'S':
    ca = float(input('Quanto você gostaria de investir?: R$'))
    te = int(input('Por quantos anos irá deixar esse capital investido?: '))
    if te <= 1:
        ju = 0.10
    elif te > 1.1 < 5:
        ju = 0.25
    elif te >= 5:
        ju == 0.45 
    mo1 = ca * (1 + ju) ** te
    mo2 = ca + mo1
    me = te * 12
    print('Calculando o valor total do seu investimento, aguarde alguns instantes... ')
    time.sleep(3)
    print(f'Pronto! Ao final você receberá um total de R${mo2:.2f}, investidos durante o período de {me} meses com um rendimento anual de {ju * 100 }%!')
    go = str(input('Gostaria de realizar outro investimento [S/N]?: ')).upper().strip()
print('Programa de simulação de rendimentos finalizado! Até breve investidor! :)')