import string
import random
letters = string.ascii_letters
numbers = str(string.digits)
chars = string.punctuation
def check_passwd(password):
        Num = 0
        Char = 0
        cap_letter = 0
        for i in numbers:
                Num += password.count(i)
        for i in chars:
                Char += password.count(i)
        for i in letters:
                cap_letter += password.count(i.upper())
        if len(password) < 7 and Num < 2 and Char < 2 and cap_letter < 1:
                return print("Invalid")
        elif len(password) >= 7 and Num >= 2 and Char >= 2 and cap_letter >= 1:
                return print("Valid")
        else:
                return print("Invalid")
while True:
        Choice = input("Validate or Create Password:")
        if Choice == "Validate" or Choice == "validate":
                print("Min requirements 2 numbers, 2 rand chars, 1 capital letter")
                Password = input("Enter a password to be checked:")
                check_passwd(Password)
        elif Choice == "Create" or Choice == "create":
                Password = ""
                Chars = letters + numbers + chars
                length = input("Enter the length of the password you want:")
                length = int(length)
                for i in range(length):
                        Password += random.choice(Chars)
                print(Password)
                                
