"""Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
Planteamiento: Crea una función que reciba dos parámetros: un número entero positivo y un exponente. La función debe calcular el número elevado al exponente dado, luego sumar todos los dígitos del resultado y devolver esa suma. Por ejemplo, si el número es 2 y el exponente es 3, calcula  2^3 = 8, y la suma de los dígitos es 8. Si el número es 5 y el exponente es 2, calcula 5^2 = 25, y la suma de los dígitos es 2 + 5 = 7."""

def suma_digitos_potencia(num, expo):
    resultado = num ** expo
    suma = 0
    for digito in str(resultado):
        suma += int(digito)
    return resultado, suma

def main():
    while True:
        try:
            num = int(input("\nIntroduce un número entero positivo (-1 para finalizar): "))
            if num == -1:
                break
            if num < 0:
                print("\nPor favor, introduce un número entero positivo.\n")
            else:
                expo = int(input("Introduce el exponente: "))
                if expo < 0:
                    print("\nEl exponente debe ser un número entero positivo.\n")
                else:
                    resultado, suma = suma_digitos_potencia(num, expo)
                    print(f"\nEl resultado de {num} {expo} es {resultado} y la suma de sus digitos es {suma}.")
        except ValueError:
            print(f"\nError. Asegúrate de introducir números enteros válidos.\n")

if __name__ == "__main__":
    main()