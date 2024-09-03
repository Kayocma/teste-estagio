def is_fibonacci_number(n):
    if n < 0:
        return False

    # Inicia a sequência de Fibonacci com os primeiros dois números
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        # Atualiza os valores de a e b para o próximo número da sequência
        a, b = b, a + b

    return False

# Solicita ao usuário para inserir um número
number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci_number(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")