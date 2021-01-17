def decimal_to_binary(number):
    binary_number = ''

    while number > 0:
        reminder = number % 2
        number = number // 2

        binary_number += str(reminder)

    return binary_number


print(decimal_to_binary(10))    # replace 10
