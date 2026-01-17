import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

length = int(input("Enter the length of Password: "))

password_characters = [random.choice(letters),
                       random.choice(numbers),
                       random.choice(symbols)]
all = letters + numbers + symbols

for i in range(length - 3):
    password_characters.append(random.choice(all))

random.shuffle(password_characters)
password = "".join(password_characters)
print("Generated Password: ", password)