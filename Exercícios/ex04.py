v = input('Coloca o valor aí tio vo detecta pa tu:')
print ('O tipo primitivo é:', type(v)) #essa naturalmente só vai detectar strings pq é um input
print ('É uma string alfabética?', v.isalpha())
print ('Tem decimais?', v.isdecimal())
print ('SÓ TEM MAIÚSCULA?', v.isupper())
print ('Só apertou espaço né danadinho tô de olho hein ;)', v.isspace())
