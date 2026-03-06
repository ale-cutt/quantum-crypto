import time

def main():
    input_name = "input.txt"
    output_name = "output.txt"
    out_f = open(output_name, 'w')
    out_f.close()
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    in_f = open(input_name, 'r')
    out_f = open(output_name, 'a')
    start = time.perf_counter()
    brute_force(in_f, out_f, alphabet) #BRUTE-FORCE
    end = time.perf_counter()
    print(f"Total Execution Time for Brute Force: {end-start}", file=out_f)
    in_f.close()
    out_f.close()
    return 

def encrypt(in_f, out_f, alphabet, encrypted_alph):
    ciphred = ''
    for line in in_f:
        for char in line:
            if char.upper() in alphabet:
                    index = alphabet.index(char.upper())
                    ciphred = ciphred + encrypted_alph[index]
            else:
                    ciphred = ciphred + char
    print(ciphred, file= out_f)
    return  

def decrypt(in_f, out_f, alphabet, encrypted_alph):
    deciphred = ''
    for line in in_f:
        for char in line:
            if char.upper() in encrypted_alph:
                index = encrypted_alph.index(char.upper())
                deciphred = deciphred + alphabet[index]
            else:
                deciphred = deciphred + char
    print(deciphred, file=out_f)
    return        

def brute_force(in_f, out_f, alphabet): #BRUTE-FORCE ATTACK: TRIES THE 26 POSSIBLE WAYS

    for key in range(26):
        encrypted_alph = []
        for i in range(26):
            encrypted_alph.append(alphabet[i-key%26])
        print(f'Key = {key+1}', file=out_f)
        in_f.seek(0) 
        decrypt(in_f, out_f, alphabet, encrypted_alph)
        print('\n', file=out_f)
    return


main()



