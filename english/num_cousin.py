def show_cousin_numbers(limit):
    order = 0

    for cousin_number in range(2, limit, 1):
        for divisor in range(2, limit, 1):
            if cousin_number % divisor == 0:
                if cousin_number == divisor:
                    order += 1
                    print(f"\n{order}°  ➜  {cousin_number:,}")
                break


finish_program = False

while not finish_program:
    try:
        limit_number = int(input("See cousin numbers from 1 to: "))

        if limit_number < 3:
            raise ValueError

    except ValueError:
        print('\nType a "number" above 3, the first cousin number is 2\n')

    else:
        show_cousin_numbers(limit_number)
        finish_program = True
