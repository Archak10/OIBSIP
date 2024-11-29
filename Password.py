import random
import string

def password_generator(length, use_letters, use_numbers, use_symbols):
    """Generates a random password based on the user's criteria."""
    if not (use_letters or use_numbers or use_symbols):
        raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")

    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = password_generator(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()