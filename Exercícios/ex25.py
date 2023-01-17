silv = str(input('Insira seu nome completo para verificar se contém SILVA nele: ')).strip().upper()
print ('Seu nome tem Silva?: {}'.format('SILVA' in silv))

# A lógica na segunda linha desse código é que o programa pegou o nome, colocou tudo em maiúsculas e procurou assim para evitar erros/outras formatações desse nome feitas pelo usuário
# Como não importa aparecer o nome na tela, usar dessa forma facilita para achar o SILVA