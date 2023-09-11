import random
import string

# hello world
print("Hello, World!")

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo: gerar senha de 12 caracteres
senha_gerada = gerar_senha(12)
print("Senha gerada:", senha_gerada)