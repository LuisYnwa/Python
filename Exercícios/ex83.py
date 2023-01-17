exp = input('Digite a expressão para ser verificada: ').strip()
valid = True
parabri = exp.count('(')
parafecha = exp.count(')')
parafecha = 0
erro = ''
if parafecha == parabri:
    for va in exp:
        if va == ')' and parafecha == 0:
            valid = False
            erro = 'Você fechou um parênteses antes de abrir!!\nTente novamente.'
            break
        else:
            if va == '(':
                parabri += 1
            if va == ')':
                parafecha -= 1
else:
    valid = False
    erro = 'A quantidade de parênteses abrindo é diferente da quantidade de parenteses fechando!!'
if parafecha > 0:
    valid = False
    erro = 'Você esqueceu de fechar um parentese'
if valid == True:
    print('A expressão está correta!!')
else:
    print(f'Sua expressão está errada!! {erro}')
