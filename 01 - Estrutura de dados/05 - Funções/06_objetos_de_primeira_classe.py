def somar(a, b):
    return a + b

def subtrair(a, b):
    return a- b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

def exibir_resultado2(a, b, funcao2):
    resultado2 = funcao2(a, b)
    print(f"O resultado da operação {a} - {b} = {resultado2}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado2(10, 10, subtrair)