# Função para descobrir o próximo elemento da sequência a)
def proximo_a(termos):
    # A lógica é que os números são ímpares consecutivos
    ultimo_termo = termos[-1]
    return ultimo_termo + 2

# Função para descobrir o próximo elemento da sequência b)
def proximo_b(termos):
    # A lógica é que cada termo é o dobro do anterior
    ultimo_termo = termos[-1]
    return ultimo_termo * 2

# Função para descobrir o próximo elemento da sequência c)
def proximo_c(termos):
    # A lógica é que os números são quadrados perfeitos: 0^2, 1^2, 2^2, 3^2, ...
    ultimo_indice = len(termos)
    return ultimo_indice ** 2

# Função para descobrir o próximo elemento da sequência d)
def proximo_d(termos):
    # A lógica é que os números são quadrados de números pares: 2^2, 4^2, 6^2, 8^2, ...
    proximo_indice_par = (len(termos) + 1) * 2
    return proximo_indice_par ** 2

# Função para descobrir o próximo elemento da sequência e)
def proximo_e(termos):
    # A lógica é que os números seguem a sequência de Fibonacci
    return termos[-1] + termos[-2]

# Função para descobrir o próximo elemento da sequência f)
def proximo_f(termos):
    # A lógica é que os números contêm o dígito '2' ou '0'
    for i in range(termos[-1] + 1, 100):  # 100 é arbitrário, apenas para evitar loops infinitos
        if '2' in str(i) or '0' in str(i):
            return i

# Dados iniciais
sequencia_a = [1, 3, 5, 7]
sequencia_b = [2, 4, 8, 16, 32, 64]
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
sequencia_d = [4, 16, 36, 64]
sequencia_e = [1, 1, 2, 3, 5, 8]
sequencia_f = [2, 10, 12, 16, 17, 18, 19]

# Calculando o próximo termo para cada sequência
print("a) Próximo termo:", proximo_a(sequencia_a))
print("b) Próximo termo:", proximo_b(sequencia_b))
print("c) Próximo termo:", proximo_c(sequencia_c))
print("d) Próximo termo:", proximo_d(sequencia_d))
print("e) Próximo termo:", proximo_e(sequencia_e))
print("f) Próximo termo:", proximo_f(sequencia_f))