def input_int(mensagem):
    while True:
        try:
            value = int(input(mensagem))
            return value
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")


def input_str(letra):
    while True:
        value = str(input(letra))
        if not value.isalpha():
            print("digite somente letras")
        else:
            return value




def input_float(nomes):
    while True:
        try:
            valor = float(input(nomes))
            return value
        except ValueError:
            print("Entrada inválida! Por favor, digite um número decimal.")

