#Gerador de senhas seguras
import random

letra_maiuscula = chr(random.randint(65, 90))  # Gera uma letra maiúscula aleatória
letra_minuscula = chr(random.randint(97, 122))  # Gera uma letra minúscula aleatória
char_especial = chr(42)  # Define um caractere especial (neste caso, o asterisco "*")
lista_numeros = []  # Cria uma lista vazia para armazenar os números gerados

for i in range(8):  # Gera 8 números aleatórios
    numeros = random.randrange(9)  # Gera um número aleatório de 0 a 9
    lista_numeros.append(numeros)  # Adiciona o número à lista de números

random.shuffle(lista_numeros)  # Embaralha a lista de números gerados
lista_numeros = str(lista_numeros)[1:-1]  # Converte a lista de números para uma string e remove os colchetes
lista_numeros = lista_numeros.replace(',', '')  # Remove as vírgulas da string de números

print(letra_maiuscula, letra_minuscula, lista_numeros, char_especial)  # Imprime a senha gerada
