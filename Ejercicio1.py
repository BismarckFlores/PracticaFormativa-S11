"""Ejercicio 1: Calcular el factorial de un número
Planteamiento: Crea una función que reciba un número entero no negativo como parámetro y devuelva su factorial. El factorial de un número n es el producto de todos los enteros positivos desde 1 hasta n (por ejemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120). Asegúrate de manejar el caso especial donde n = 0, que devuelve 1."""

def factorial(n):
    if n == 0:
        return 1
    
    resultado = 1
    for num in range(1, n + 1):
        resultado *= num
    return resultado

def main():
    while True:
        try:
            num = int(input("\nIntroduce un número entero no negativo (-1 para finalizar): "))
            if num == -1:
                break
            if num < 0:
                print("\nPor favor, introduce un número entero no negativo.\n")
            else:
                print(f"\nEl factorial de {num} es {factorial(num)}\n")
        except ValueError:
            print(f"\nError. Asegúrate de introducir un número entero válido.\n")

if __name__ == "__main__":
    main()