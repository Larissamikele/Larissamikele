# Inicializando a variável soma e o contador x
soma = 0
x = 1

# Laço de repetição que percorre os 100 primeiros números inteiros positivos
while x <= 100:
    soma += x  # Adiciona o valor de x à soma
    x += 1     # Incrementa x em 1

# Exibindo o resultado após o fim do laço
print(f'A soma dos 100 primeiros números inteiros positivos é {soma}.')
