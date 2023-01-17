from random import randrange 
jkp = int(input('Digite [1] para tesoura, [2] para pedra e [3] para papel para jogarmos!!'))
s = randrange(1,4) #o número final sempre tem que ser +1 do que o considerado na vida real para essa função funcionar
if jkp == s:
    print(f'O computador também selecionou {jkp}, então vocês empataram!!')
elif jkp == 1 and s == 2: 
    print('Você perdeu! A pedra quebra a tesoura!!')
elif jkp == 1 and s == 3:
    print('Você ganhou! A tesoura corta o papel!!')
elif jkp == 2 and s == 3:
    print('Você perdeu! O papel enrola a pedra!!')
elif jkp == 2 and s == 1:
    print('Você ganhou! A pedra quebra a tesoura!!')
elif jkp == 3 and s == 1:
    print('Você perdeu! A tesoura corta o papel!!')
elif jkp == 3 and s == 2:
    print('Você ganhou! O papel enrola a pedra!!')