from datetime import date
con = 0
conma = 0
conme = 0
for p in range (1, 8):
    an = int(input(f'Insira o ano de nascimento da {p}° pessoa:'))
    sub = date.today().year - an
    con = con + 1
    if sub >= 18:
        conma += 1
    elif sub<= 18:
        conme += 1
print(f'Ao todo, {conma} pessoas são maiores de idade e {conme} são menores de idade')