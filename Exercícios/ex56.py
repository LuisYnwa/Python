vel = 0
veln = 0
for ag in range (1,5):
    print (f'-----{ag}° PESSOA -----')
    ida = int(input(f'Insira a idade da {ag}° pessoa: ')) 
    if ag == 1: #idade do mais velho
        vel = ida
        veln = ida
    else:
        if ida > vel:
            vel = ida
print(f'O mais velho tem {vel} anos!!')