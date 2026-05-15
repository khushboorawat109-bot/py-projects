import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
all_characters = lower + upper + digits + special
length = int(input("Enter the desired password length: "))
if length < 4:
    print("Password length should be at least 4 to include all character types.")
else:
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    final_password = ''.join(password)
    print("Generated Password: ", final_password)


