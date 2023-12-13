"""
Program for password hashing to be used on the password cracking website
"""
import hashlib


def hash_password(password):
    """
    Takes the password the user entered
    then encodes it and hashes with:
    MD5
    SHA-256
    SHA-512
    """
    # Encode the password to bytes using UTF-8 encoding
    password_bytes = password.encode()

    # Hash with MD5, SHA-256, and SHA-512
    md5_hash = hashlib.md5(password_bytes).hexdigest()
    sha256_hash = hashlib.sha256(password_bytes).hexdigest()
    sha512_hash = hashlib.sha512(password_bytes).hexdigest()

    return md5_hash, sha256_hash, sha512_hash


def password_cracking_activity():
    """
    function to ask user for password to encode
    Then prints the encoded password in:
    MD5
    SHA-256
    SHA-512
    """
    print("Enter a password to encode:")
    user_password = input()

    md5_hash, sha256_hash, sha512_hash = hash_password(user_password)

    print(f"MD5 Hash: {md5_hash}")
    print(f"SHA-256 Hash: {sha256_hash}")
    print(f"SHA-512 Hash: {sha512_hash}")


if __name__ == "__main__":
    password_cracking_activity()
