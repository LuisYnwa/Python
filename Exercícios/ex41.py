from datetime import date

id = int(input('Insira o ano que você nasceu: '))
da = date.today().year
cat = da - id
if cat <= 9:
    print(f'Você entrará na categoria MIRIM já que tem apenas {cat} anos')
elif cat <= 14:
    print(f'Você entrará na categoria INFANTIL já que tem apenas {cat} anos')
elif cat <= 17:
    print(f'Você entrará na categoria JÚNIOR já que tem {cat} anos')
elif cat <= 20:
    print(f'Você entrará direto na categoria SÊNIOR já que tem {cat} anos')
else:
    print(f'Você já tem mais de {cat} anos, então entrará diretamente na categoria MASTER!')