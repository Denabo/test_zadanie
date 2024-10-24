def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


def find_max_sum_number():
    max_sum = -1
    max_number = None

    while True:
        num = int(input("Введите целое число (0 для завершения): "))
        if num == 0:
            break

        current_sum = sum_of_digits(num)
        if current_sum > max_sum:
            max_sum = current_sum
            max_number = num

    print(f"Число с максимальной суммой цифр: {max_number}")


if __name__ == "__main__":
    find_max_sum_number()
