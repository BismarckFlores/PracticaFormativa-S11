"""Ejercicio 2: Convertir un número decimal a binario
Planteamiento: Escribe una función que reciba un número entero positivo y devuelva una cadena con su representación en binario (base 2). Por ejemplo, si se ingresa 10, la función debe devolver "1010". No uses funciones integradas de conversión a binario; implementa la lógica dividiendo el número y construyendo la cadena manualmente."""

def decimal_a_binario(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

def main():
    while True:
        try:
            num = int(input("\nIntroduce un número entero positivo (-1 para finalizar): "))
            if num == -1:
                break
            if num < 0:
                print("\nPor favor, introduce un número entero positivo.\n")
            else:
                print(f"\nLa representación en binario de {num} es {decimal_a_binario(num)}\n")
        except ValueError:
            print(f"\nError. Asegúrate de introducir un número entero válido.\n")