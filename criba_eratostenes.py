import argparse

def criba_eratostenes(n):
    # Creamos una lista de booleanos inicializada en True para representar todos los números de 2 a n como números primos
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False  # 0 y 1 no son primos
    
    p = 2
    while p * p <= n:
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

    # Generamos una lista de números primos
    numeros_primos = []
    for i in range(2, n + 1):
        if primos[i]:
            numeros_primos.append(i)

    return numeros_primos

def main():
    parser = argparse.ArgumentParser(description="Encuentra números primos hasta un límite superior.")
    parser.add_argument("-l", "--limite", type=int, help="Límite superior para encontrar números primos.")
    args = parser.parse_args()

    if args.limite is not None:
        limite_superior = args.limite
    else:
        limite_superior = int(input("Ingrese el límite superior: "))

    primos_hasta_limite = criba_eratostenes(limite_superior)
    
    print(f"Números primos hasta {limite_superior}:")
    print(primos_hasta_limite)

if __name__ == "__main__":
    main()
