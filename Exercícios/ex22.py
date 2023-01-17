nom = str (input ('Insira seu nome completo: '))
nomlo = nom.lower()
nomup = nom.upper()
nomspli = nom.split()
print (f"""Seu nome em minúsculas é {nomlo}
Seu nome em maiúsculas é {nomup} 
A quantidade de caracteres no seu nome é:{(len(''.join(nomspli)))} 
E seu primeiro nome tem {(len(nomspli[0]))} letras""")

# Na linha 7 a logica foi de separar o nome bloquinhos com a split(em variável) e após isso junta-la através do join e do '' sem espaço dentro, juntando assim todos os blocos e colocando o len para contar
# Enquanto isso na linha 8 o len lê o nome splitado e procura a quantidade de caracteres no primeiro nome (no caso 0 pois na computação é onde ocorre o primeiro processo em vez do 1)