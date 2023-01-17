x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))
z = int(input('Insira o terceiro número: '))
ma = x
#Aqui eu basicamente defino um valor como o maior de todos e o resto dos IF vão desmentindo minha informação e mostrando qual é o verdadeiro
if y > x and y > z:
    ma = y
if z > x and z > y:
    ma = z
print (f'O maior número é: {ma}')
#A mesma lógica segue para o valor menor
meno = y
if x < y and x < z:
    meno = x
if z < y and z < x:
    meno = z
print (f'O menor valor é: {meno}')