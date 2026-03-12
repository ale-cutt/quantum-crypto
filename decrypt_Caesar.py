#Function used to decrypt a ciphertext encrypted with Caesar's Cipher given a certain key k
#in_f is the file containing the ciphertext we want to decrypt
#out_f is the file where the decrypted text will be printed

import alphabet

def decrypt_Caesar(in_f, out_f, k):
    deciphred = ''
    for line in in_f:
        for char in line:
            upper_char = char.upper()
            if upper_char in alphabet:
                deciphred += alphabet[(alphabet.index(upper_char) - k) % 26]
            else:
                deciphred += char
    print(deciphred, file=out_f)
    return        
