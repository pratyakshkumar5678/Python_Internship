import sys
from cryptography.fernet import Fernet

def genkey(path):
    k = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(k)
    print(f"Key saved to {path}")

def encrypt(keyfile, infile, outfile):
    with open(keyfile, "rb") as kf:
        key = kf.read()
    f = Fernet(key)
    with open(infile, "rb") as f_in:
        data = f_in.read()
    token = f.encrypt(data)
    with open(outfile, "wb") as f_out:
        f_out.write(token)
    print(f"Encrypted -> {outfile}")

def decrypt(keyfile, infile, outfile):
    with open(keyfile, "rb") as kf:
        key = kf.read()
    f = Fernet(key)
    with open(infile, "rb") as f_in:
        token = f_in.read()
    data = f.decrypt(token)
    with open(outfile, "wb") as f_out:
        f_out.write(data)
    print(f"Decrypted -> {outfile}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python file_encrypt.py <genkey|encrypt|decrypt> ...")
        return
    cmd = sys.argv[1]
    if cmd == "genkey":
        genkey(sys.argv[2])
    elif cmd == "encrypt":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "decrypt":
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
