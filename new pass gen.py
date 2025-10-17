"""
==============================
      Python Password Generator
==============================
Welcome! Create a strong password in seconds.
==============================
"""

import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        try:
            length_input = input("Enter desired password length (or 'Exit' to quit): ").strip()
            if length_input.lower() == 'exit':
                print("Thank you for using the Password Generator. Stay safe!")
                break
            length = int(length_input)
            password = generate_password(length)
            if password:
                print(f"\nYour new password: \033[1;32m{password}\033[0m")
                print("-"*30)
        except ValueError:
            print("Please enter a valid number.")
            print("-"*30)

if __name__ == "__main__":
    main()
