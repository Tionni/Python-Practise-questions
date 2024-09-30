def get_sum_squares(numbers):
    return sum([number ** 2 for number in numbers])

numbers = [1, 2, 3, 4]
print(get_sum_squares(numbers))  # Expected output: 30
