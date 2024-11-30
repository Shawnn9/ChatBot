from cryptography.fernet import Fernet

# Load the encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Read the encrypted file
with open("questions_encrypted.json", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the file data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Write the decrypted data to a new file (optional)
with open("questions_decrypted.json", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully.")
