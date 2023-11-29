import random
import string

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    # Define character sets based on user preferences
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if uppercase else ''
    digit_chars = string.digits if digits else ''
    symbol_chars = string.punctuation if symbols else ''

    # Ensure at least one character from each selected category
    password = [random.choice(lower_chars)]

    # Add an uppercase letter if selected
    if uppercase:
        password.append(random.choice(upper_chars))

    # Add a digit if selected
    if digits:
        password.append(random.choice(digit_chars))

    # Add a symbol if selected
    if symbols:
        password.append(random.choice(symbol_chars))

    # Generate the rest of the password
    all_chars = lower_chars + upper_chars + digit_chars + symbol_chars
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)
    return password_str

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Check if none of the options are selected
    if not include_uppercase and not include_digits and not include_symbols:
        print("At least one category (uppercase, digits, or symbols) must be selected.")
    else:
        generated_password = generate_password(password_length, include_uppercase, include_digits, include_symbols)
        print(f"Generated Password: {generated_password}")
