dias = int (input('Por quantos dias você usou o carro?: '))
klm = float (input('Por quantos kilometros? '))
fim = (dias * 60) + (klm * 5)
print (F'O valor total a ser pago é de R${fim}')
