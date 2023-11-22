import hashlib


def hash_password(password):
    # Hash the password using MD5, SHA-256, and SHA-512
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()
    return md5_hash, sha256_hash, sha512_hash


def main_password_cracking_activity():
    # List of passwords for testing
    passwords = ["password01", "hello05", "strongP@ssword", "mySecureP@ss"]

    print("Table 1. Password Cracking Activity Results")
    print("Password\t\tMD5 Hash\t\t\tSHA-256 Hash\t\t\tSHA-512 Hash\t\t\tDid Crackstation work?")

    for password in passwords:
        md5_hash, sha256_hash, sha512_hash = hash_password(password)

        print(
            f"{password}\t\t{md5_hash}\t{sha256_hash}\t{sha512_hash}\t{check_crackstation(md5_hash, sha256_hash, sha512_hash)}")


def check_crackstation(*hashes):
    # You can implement a function to check if the hashes are cracked using an online service
    # For simplicity, you can return "Yes" if any of the hashes are cracked, else "No"
    # Implement this based on your preferred approach or external service.
    return "Yes" if any(crack_hash(hash) for hash in hashes) else "No"


def crack_hash(hash):
    # Implement logic to check if the hash is cracked using an online service
    # For simplicity, this function returns True if the hash is cracked, else False
    # Implement this based on your preferred approach or external service.
    return False


if __name__ == "__main__":
    main_password_cracking_activity()
