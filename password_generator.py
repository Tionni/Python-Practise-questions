import random
def generate_password(length_of_password):
    lower_case ='abcdefghijklmnopqrstuvwxyz'
    lowercase_length  = len(lower_case)
    upper_case ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    uppercase_length = len(upper_case)
    numbers = '0123456789'
    numbers_length =  len(numbers)
    symbols = '!@#$^&*?'
    symbols_length = len(symbols)

    password = ""
    count = 1
    while(count <= length_of_password ):
        choice = random.randint(1, 4)
        if choice == 1:
            index_lower = random.randint(0, lowercase_length - 1)
            password = password + lower_case[index_lower]
        elif choice == 2:
            index_upper = random.randint(0, uppercase_length - 1)
            password = password + upper_case[index_upper]
        elif choice == 3:
            index_number = random.randint(0, numbers_length - 1)
            password = password + numbers[index_number]
        else:
            index_symbols = random.randint(0, symbols_length - 1)
            password = password + symbols[index_symbols]


        count = count + 1

    return password  

def main():
    print("Enter length of characters") 
    n = int(input())
    print(generate_password(n))
 
if __name__ == '__main__':
    main()


