
def generar_fibonacci(n):
    """Genera una lista con los primeros n términos de Fibonacci."""
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie


def main():
    print("     PROGRAMA: SERIE DE FIBONACCI")

    n = int(input("Ingresa la cantidad de términos que deseas generar: "))

    if n <= 0:
        print("Debes ingresar un número entero positivo.")
    else:
        serie = generar_fibonacci(n)
        print("\nSerie de Fibonacci con", n, "términos:")
        for numero in serie:
            print(numero, end=" ")
        print("\n\nseire finalizada.")

if __name__ == "__main__":
    main()