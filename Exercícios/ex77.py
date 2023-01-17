pala = ('João', 'estudar', 'frequentar', 'amostra', 'planilha', 'lugar', 'morcego', 'canais')
for pa in pala:
    print(f'\nA palavra {pa.upper()} tem como vogais:', end=' ')
    for vog in pa:
        if vog.lower() in 'aeiou':
            print(vog, end=' ')
