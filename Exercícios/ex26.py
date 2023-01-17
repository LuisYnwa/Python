import unicodedata
fra = str (input ('Insira uma frase: ')).lower().strip()
As = fra.count('a') 
print (f'A letra A aparece na frase {As} vezes')
f1 = int (fra.find('a')+1)
print (f'Ela aparece pela primeira vez na posição: {f1}')
f2 = int (fra.rfind('a')+1)
print (f'Ela aparece pela primeira vez na posição: {f2}')
#first, *middle, last = fra.split()

#Da para adaptar os A acentuados utilizando também o unicode porém não consegui usar
