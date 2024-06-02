def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        if ord(string[i]) == 32:
            cipher_text.append(chr(32))
        else:
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
    return "".join(cipher_text)

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if ord(cipher_text[i]) == 32:
            orig_text.append(chr(32))
        else:
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
    return "".join(orig_text)

plaintext = input("Enter plain text: ").upper()
key = input("Enter keyword: ").upper()
key = generateKey(plaintext, key)
encrypted_text = cipherText(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = originalText(encrypted_text, key)
print("Decrypted text:", decrypted_text)
