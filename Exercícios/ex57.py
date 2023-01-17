#quebrado porque não conta
g = 'S'
conM = 0
conF = 0
while g == 'S':
    se = str(input('Qual é o sexo dessa pessoa? (M/F): ')).upper().strip()
    if se == 'M':
        conM =+ 1
    elif se == 'F':
        conF =+ 1
    g = str(input('Você deseja continuar? (S/N): ')).upper().strip()
print(f'Ao todo, você digitou {conM} pessoas do sexo MASCULINO e {conF} pessoas do sexo FEMININO!!')    

#código para validação abaixo
#else:
    #str(input('Você digitou um valor inválido! Tente novamente utilizando M para masculino e F para #feminino'))

