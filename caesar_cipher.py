def caesar_cipher(text,shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    
    return result 

print("*CAESAR CIPHER PROGRAM*")

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift amount: "))
    mode = input("Do you want to encrypt or decrypt? ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"The result is: {result}")

# Ensure this block runs only when the script is executed directly
if __name__ == "__main__":
    main()
