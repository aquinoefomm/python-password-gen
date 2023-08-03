import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("-" * 36)
print("WELCOME TO THE PyPASSWORD GENERATOR!")
print("-" * 36)
nr_letters = int(input("How many letters do you want? "))
nr_symbols = int(input("How many symbols do you want? "))
nr_numbers = int(input("How many numbers do you want? "))
total_char = nr_letters + nr_symbols + nr_numbers

chosen_letters = []
chosen_symbols = []
chosen_numbers = []
chosen_chars =[]

for c in range(1, nr_letters + 1):
    for index in range(0, nr_letters):
        i = random.randint(0, len(letters) - 1)
    chosen_letters.append(letters[i])
print(chosen_letters)
for c in range(1, nr_symbols + 1):
    for index in range(0, nr_symbols):
        i = random.randint(0, len(symbols) - 1)
    chosen_symbols.append(symbols[i])
print(chosen_symbols)
for c in range(1, nr_numbers + 1):
    for index in range(0, nr_numbers):
        i = random.randint(0, len(numbers) - 1)
    chosen_numbers.append(numbers[i])
print(chosen_numbers)

for l in chosen_letters:
    chosen_chars.append(l)
for s in chosen_symbols:
    chosen_chars.append(s)
for n in chosen_numbers:
    chosen_chars.append(n)
print(chosen_chars)

random.shuffle(chosen_chars)

gen_password = ''.join(chosen_chars)
# for c in chosen_chars:
#     gen_password += c
print(f'This is your password: {gen_password}')




