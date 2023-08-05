#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
usr_letters= int(input("How many letters would you like in your password?\n")) 
usr_symbols = int(input(f"How many symbols would you like?\n"))
usr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for char in range(1, usr_letters +1):
    # random_char = random.choice(letters)
    password += random.choice(letters)

for symbol in range(1, usr_symbols +1):
    password += random.choice(symbols)

for number in range(1, usr_numbers +1):
    password+= random.choice(numbers)

print(password)

#Withlout using loops
letter = random.choices(letters, k=usr_letters)
letters_joined = "".join(letter)
print(letters_joined)

number = random.choices(numbers, k=usr_numbers)
numbers_joined = "".join(number)
print(numbers_joined)

symbol = random.choices(symbols, k=usr_symbols)
symbols_joined = "".join(symbol)
print(symbols_joined)

Final_password = letters_joined + numbers_joined + symbols_joined
print(Final_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for char in range(1, usr_letters +1):
    # random_char = random.choice(letters)
    # password += random_char
    password += random.choice(letters)

for symbol in range(1, usr_symbols +1):
    password += random.choice(symbols)

for number in range(1, usr_numbers +1):
    password+= random.choice(numbers)

random.shuffle(password)

shuffled_password = "".join(password)

print(shuffled_password)


#Testing shuffle function:
# password_test = ['C', '&', 'L', '%', '6', '!', '0', 'd', '9', '8', 'u', 'b', '(', '#', '2']
# random.shuffle(password_test)

# final_password = "".join(password_test)
# print(password_test)
# print(final_password)


















