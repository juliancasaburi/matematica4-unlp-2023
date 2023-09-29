import argparse

def euclides(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    parser = argparse.ArgumentParser(description="Encuentra el MCD de dos números enteros utilizando el algoritmo de Euclides.")
    parser.add_argument("num1", type=int, nargs="?", default=None, help="Primer número entero")
    parser.add_argument("num2", type=int, nargs="?", default=None, help="Segundo número entero")
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2

    if num1 is None:
        num1 = int(input("Ingresa el primer número entero: "))
    if num2 is None:
        num2 = int(input("Ingresa el segundo número entero: "))

    mcd = euclides(num1, num2)
    print(f"El MCD de {num1} y {num2} es {mcd}")

if __name__ == "__main__":
    main()
