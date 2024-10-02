#prime number is a number without divisor

# def return_divisor(number):
#     divisor = []
#     for num in range(number, 1, -1):
#         if (number % num == 0):
#             divisor.append(num)
#     return divisor

#using list comprehension
def return_divisor(number):
    return [num for num in range(number, 1, -1) if (number % num == 0)]

#if a number is prime it willbe divisible
#one or it self. for the function above it returns only one
#divisor if it is prime
print("Enter a number")
number = int(input())

if len(return_divisor(number)) == 1:
    print(str(number) + " is a prime number ")
else:
     print(str(number) + " is not a prime number ")
