import math
ang = int (input('Digite o valor do ângulo: '))
ang2 = math.radians (ang)
sin = math.sin(ang2)
cos = math.cos(ang2)
tan = math.tan(ang2)
print (f'O ângulo de {ang}° tem o {sin:.2} de seno, o {cos:.2} de cosseno e o {tan:.2} de tangente')