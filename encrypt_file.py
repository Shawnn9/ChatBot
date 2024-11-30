from cryptography.fernet import Fernet

# Generate and save the encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key securely in a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Read the JSON file with questions and answers
with open("questions.json", "rb") as file:
    file_data = file.read()

# Encrypt the file data
encrypted_data = cipher_suite.encrypt(file_data)

# Save the encrypted data to a new file
with open("questions_encrypted.json", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully.")
