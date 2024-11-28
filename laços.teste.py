''' Solicitar um numero inteiro e calcule o seu fatorial'''

numero= int(input('infome um numero inteiro: '))
def fatorial (n):   
    if n == 0 or n == 1: 
        return 1
    
    else: 
         return n * fatorial(n - 1)

resultado = fatorial(numero)

print(f'O fatorial de {numero} é {resultado}')
