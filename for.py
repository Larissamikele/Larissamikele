import sys

# Solicitar o número de primos desejados
n = int(input('Quantos números primos deseja gerar? '))

# Verificar se o número de primos solicitado é válido
if n <= 0:
    sys.exit('Por favor, forneça um número maior que 0.')

cont_primos = 0
numero = 2

# Laço para encontrar e imprimir os números primos
while cont_primos < n:
    cont_divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont_divisores += 1

    # Se o número tem exatamente 2 divisores, é primo
    if cont_divisores == 2:
        print(numero)
        cont_primos += 1

    # Incrementar para verificar o próximo número
    numero += 1
