def verificar_letra_a(string):
    # Contar ocorrências de 'a' e 'A'
    contagem_a_minuscula = string.count('a')
    contagem_a_maiuscula = string.count('A')
    contagem_total = contagem_a_minuscula + contagem_a_maiuscula
    
    # Verificar se a letra 'a' está presente
    if contagem_total > 0:
        print(f"A letra 'a' aparece {contagem_total} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Solicitar ao usuário que insira uma string
texto = input("Digite uma string: ")

# Chamar a função para verificar a string
verificar_letra_a(texto)