tab = ('Cuiabá', 'Santos', 'Flamengo', 'América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo')
print(f'Os 5 primeiros colocados são: {tab [0:5]}')
print('---'*20)
print(f'Os times que estão na zona de rebaixamento são: {tab [16:20]}')
print('---'*20)
print(f'A tabela organizada em ordem alfabética fica: {sorted(tab)}')
print('---'*20)
print(f'O Bragantino está na {tab.index("Bragantino") + 1}° posição na tabela')
