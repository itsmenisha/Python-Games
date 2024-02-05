# password generation

import random
character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
password_list = []
charnum = int(input("enter the number of characters you want:"))
numbernum = int(input("How many numbers do you want:"))
symbolnum = int(input("enter the number symbol of  you want:"))

for n in range(1, charnum+1):
    password_list.append(random.choice(character_list))
for n in range(1, numbernum+1):
    password_list.append(random.choice(number_list))
for n in range(1, symbolnum+1):
    password_list.append(random.choice(symbol_list))

print(password_list)
random.shuffle(password_list)
print(password_list)
# harder one
password = " "
for char in password_list:
    password += char

print(f"THE PASSWORD IS :{password}")
