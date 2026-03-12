#Function used to brute-force Caesar's Cipher: tries all of the 26 different possible encryptions
#input_name is the name of the file containing the ciphertext, output_name is the name of the file where the result of the brute-force attack will be printed

import time
import decrypt_Caesar

def brute_force_Caesar(input_name, output_name): 

    out_f = open(output_name, 'w')
    out_f.close()
    
    in_f = open(input_name, 'r')
    out_f = open(output_name, 'a')
    start = time.perf_counter()
    
    for key in range(26):
        print(f'Key = {key+1}', file=out_f)
        in_f.seek(0) 
        decrypt_Caesar.decrypt_Caesar(in_f, out_f, key)
        print('\n', file=out_f)

    end = time.perf_counter()
    print(f"Total Execution Time for Brute Force: {end-start}", file=out_f)
    in_f.close()
    out_f.close()
    return
