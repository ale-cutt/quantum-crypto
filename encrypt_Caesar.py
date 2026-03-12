#Function used to encrypt a plaintext using Caesar's Cipher given a certain key k
#in_f is the file containing the plaintext we want to encrypt
#out_f is the file where the ciphertext will be printed

import alphabet

def encrypt_Caesar(in_f, out_f, k):
    ciphred = ''
    for line in in_f:
        for char in line:
            upper_char = char.upper()
            if upper_char in alphabet:
                ciphred+= alphabet[(alphabet.index(upper_char)+k)%26]
            else:
                ciphred += char
    print(ciphred, file= out_f)
    return  