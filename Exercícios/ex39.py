from datetime import date
an = int (input('Em que ano você nasceu?: '))
d = date.today().year - an
if d < 18:
    f = 18 - d
    print (f'Você ainda não precisa se alistar no exército pois tem apenas {d} anos! Se livrou dessa hein!!')
    print (f'Só precisará se alistar daqui {f} anos!')
elif d == 18:
    print(f'Você terá que se alistar esse ano pois completará/completou 18!')
else:
    a = d - 18
    print(f'Você já passou {a} anos do alistamento! Abre o olho hein garoto!!')