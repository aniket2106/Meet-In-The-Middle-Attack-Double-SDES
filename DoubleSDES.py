import OEP
if __name__ == "__main__":
    print('Enter key 1 (K1): ',end='')
    key = [int(i) for i in input()]
    print('Enter key 2 (K2): ',end='')
    key2 = [int(i) for i in input()]
    
    print('Enter plain text: ',end='')
    plainText = [int(i) for i in input()]
    print(f"Plaintext: {plainText}")

    # -Single Encryption
    ip = OEP.getPermute(plainText, 'IP')
    k1,k2 = OEP.getKey(key)
    roundOneEncryption = OEP.getEncryption(ip, k1, k2) 
    print(f"Intermediate Cipher Text: {roundOneEncryption}")

    ip2 = OEP.getPermute(roundOneEncryption, 'IP')
    k1,k2 = OEP.getKey(key2)
    roundTwoEncryption = OEP.getEncryption(ip2, k1, k2) 
    print(f"Final Cipher Text:        {roundTwoEncryption}")

    # -Decrpytion starts from here.
    print('\nEnter Cipher text: ',end='')
    cipherText = [int(i) for i in input()]
    ip = OEP.getPermute(cipherText, 'IP')
    k1,k2 = OEP.getKey(key2)
    roundOneDecryption = OEP.getDecryption(ip, k1, k2) 
    print(f"Intermediate DeCipher Text: {roundOneDecryption}")

    ip2 = OEP.getPermute(roundOneDecryption, 'IP')
    k1,k2 = OEP.getKey(key)
    roundTwoDecryption = OEP.getDecryption(ip2, k1, k2) 
    print(f"Final DeCipher Text:        {roundTwoDecryption}")