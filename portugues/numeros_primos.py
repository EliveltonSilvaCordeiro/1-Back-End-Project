def mostrar_numeros_primos(limit):
    ordem = 0

    for numeros_primos in range(2, limit):
        for divisor in range(2, limit):
            if numeros_primos % divisor == 0:
                if numeros_primos == divisor:
                    ordem += 1
                    print(f"\n{ordem}°  ➜  {numeros_primos:,}")
                break


finalizar_progama = False

while not finalizar_progama:
    try:
        numero_limitador = int(input("Ver números primos de 1 a: "))

        if numero_limitador < 3:
            raise ValueError

    except ValueError:
        print('\nDigite um "número" acima de 3, o primeiro número primo é 2\n')

    else:
        mostrar_numeros_primos(numero_limitador)
        finalizar_progama = True
