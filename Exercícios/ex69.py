cont = 0
contm = 0
contf = 0
contdezo = 0
old = 0
oldn = 0
while True:
    cont += 1
    age = int(input(f'Qual é a idade da {cont} pessoa?: '))
    if age >= 18:
        contdezo += 1
    sex = str(input(f'E o sexo dela? [M/F]: ')).upper().strip()
    if sex == 'M':
        contm += 1
    elif sex == 'F' and age < 20:
        contf += 1
    go = str(input('Você gostaria de continuar? [S/N] ')).upper().strip()
    if go == 'N':
        print(f'Obrigado por participar!! {contdezo} pessoas eram maiores de idade \n{contm} homens foram cadastrados \n{contf} mulheres tinham menos de 20 anos ')
        break
