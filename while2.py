 '''Fazer um programa que fique solicitando ao usuário para digitar um número
   inteiro e informe se o número é par ou ímpar. 
   
   O programa só deve encerrar quando o usuário digitar o número 0.
'''

while True:
    n = int(input("Informe um número para defini-lo como par ou ímpar: "))

    if n == 0:
        break
    if n % 2 == 0:
        print(f'{n} é um número par!')
    else:
        print(f'{n} é um número ímpar!')
