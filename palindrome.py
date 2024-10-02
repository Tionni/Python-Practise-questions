def palindrome_check(s):
    reverse = s[: :-1]
    if reverse == s:
        print(s + " is palidrome")
    else:
        print(s + "is not palidrome")

print("Enter a string")
s = input()        
palindrome_check(s)