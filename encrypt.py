from cryptography.fernet import Fernet


def encrypt_password(password, encryption_key):
    # Ensure the key is 32 bytes and URL-safe base64-encoded
    cipher_suite = Fernet(encryption_key)
    # Encrypt the password
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password, encryption_key.decode('utf-8')


def main():
    # Get input from the user
    to_be_encrypted = "add_whatever_you_wish_to_encrypt_here"

    # Specify the encryption key you want to use
    encryption_key = b'add_encryption_key_here'
    # Encrypt the password
    encrypted_password, key = encrypt_password(to_be_encrypted, encryption_key)
    # Print the encrypted password and the key
    print("Encrypted Password:", encrypted_password)
    print("Encryption Key:", key)


if __name__ == "__main__":
    main()
