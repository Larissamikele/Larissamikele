...

#EXEMPLO 01:
   #Fazer um programa em que o usuário informe uma string e em seguida
   #o programa informe quantos carateres existem na string digitada

...

frase = input('Informe uma frase: ')
intQtVogais = 0 
intPosicao = 0 

while intPosicao < len(frase): 
    if frase[intPosicao].lower() in 'aeiou': 
        intQtVogais += 1
    intPosicao += 1

print(f'A frase contém {intQtVogais} vogais.')
