num = int(input ('Insira aqui um número com até 4 digitos: '))
n1 = num // 1 % 10
n2 = num //10 % 10
n3 = num //100 % 10
n4 = num //1000 % 10

print (f"Analisando o número {num}...\n Unidade: {n1} \n Dezena: {n2} \n Centena: {n3}\n Milhar: {n4} ")