print("Enter a number")
number = int(input())
divisor = []
for num in range(number, 1, -1):
    if (number % num == 0):
        divisor.append(num)
print(divisor)