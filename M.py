def get_number_from_user() -> int:
    number_from_user = input("Enter an int number:")
    return int(number_from_user)


def sum_digits(number: int) -> int:
    digits_sum = 0
    while number:
        least_significant_digit = number % 10
        digits_sum += least_significant_digit
        number = number // 10
    return digits_sum


number_from_user = get_number_from_user()
sum_of_digits = sum_digits(number_from_user)
print("The sum of digit in %d is %d" % (number_from_user, sum_of_digits))
