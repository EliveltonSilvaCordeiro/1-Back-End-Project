if "__name__" == "__main__":
    main = ()


def showCousin(limit):
    guidePrime = 1
    order = 0

    for cousin in range(2, limit, 1):
        for divisor in range(2, limit, 1):
            if cousin % divisor == 0:
                if guidePrime == 1:
                    guidePrime = 0
                    if cousin == divisor:
                        order += 1
                        print(f"\n{order}°  ➜  {cousin:,}")
                    break
                else:
                    guidePrime = + 1



limit = int(input("Ver números primos de 1 a: "))

showCousin(limit)
