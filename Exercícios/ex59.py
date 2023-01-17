val1 = float(input('Insira o primeiro valor: '))
val2 = float(input('Insira o segundo valor: '))
print('[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
menu = int(input('Qual operação você irá utilizar?:'))
while menu != 5:
    if menu == 1:
        r1 = val1 + val2
        print('[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
        menu = int(input(f'O resultado dessa operação foi {r1}!! Gostaria de realizar outra?: '))
    elif menu == 2:
        r2 = val1 * val2
        print('Comandos:\n[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
        menu = int(input(f'O resultado dessa operação foi de {r2}!! Gostaria de realizar outra?:'))
    elif menu == 3:
        if val1 > val2:
            print('Comandos:\n[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
            menu = int(input(f'O maior valor é {val1}!! Gostaria de realizar otura operação?: '))
        elif val1 < val2:
            print('Comandos:\n[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
            menu = int(input(f'O maior valor é {val2}!! Gostaria de realizar outra operação?: '))
        else:
            print('Comandos:\n[1] para somar\n[2] para multiplicar\n[3] para pegar o maior\n[4] para escolher novos números\n[5] para sair do programa: ')
            menu = int(input('Os valores são iguais!! Gostaria de tentar otura operação?: '))
    elif menu == 4:
        val1 = float(input('Insira o primeiro valor: '))
        val2 = float(input('Insira o segundo valor: '))
        menu = int(input('Qual operação você irá utilizar?: '))
print('O programa encerrou!')

