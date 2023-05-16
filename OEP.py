import sys
def getPermute(lst, n):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    P4 = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IPIN = [4, 1, 3, 5, 7, 2, 8, 6]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]

    ret = []

    if n == 'P10':
        for i in P10:
            ret.append(lst[i - 1])

    elif n == 'P8':
        for i in P8:
            ret.append(lst[i - 1])

    elif n == 'P4':
        for i in P4:
            ret.append(lst[i - 1])

    elif n == 'IP':
        for i in IP:
            ret.append(lst[i - 1])

    elif n == 'IPIN':
        for i in IPIN:
            ret.append(lst[i - 1])

    elif n == 'EP':
        for i in EP:
            ret.append(lst[i - 1])

    return ret


def leftShift(lst):
    a = lst.pop(0)
    lst.append(a)
    return lst


def FK(ip,key):
    ipL = ip[:4]
    ipR = ip[4:]

    S0 = [[1,0,3,2], [3,2,1,0], [0,2,1,3], [3,1,3,2]]
    S1 = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]

    ep = getPermute(ipR, 'EP')

    xor = []
    for i in range(len(ep)):
        xor.append(ep[i] ^ key[i])

    #xorL = S0 & xorR = S1
    xorL = xor[:4]
    xorR = xor[4:]

    t1 = str(xorL[0]) + str(xorL[3])   #'00' 
    t2 = str(xorL[1]) + str(xorL[2])   #'00'
    t3 = str(xorR[0]) + str(xorR[3])   #'00' 
    t4 = str(xorR[1]) + str(xorR[2])   #'00'

    decToBin = {0:'00',1:'01',2:'10',3:'11'}
    binToDec = {'00':0,'01':1,'10':2,'11':3}
    
    PreP4 = decToBin[S0[binToDec[t1]][binToDec[t2]]] + decToBin[S1[binToDec[t3]][binToDec[t4]]]

    PreP4 = [int(i) for i in PreP4]
    P4 = getPermute(PreP4,'P4')

    xor2 = []
    for i in range(len(P4)):
        xor2.append(ipL[i] ^ P4[i])
    
    IM = xor2 + ipR

    return IM

def getEncryption(ip,k1,k2):
    InterMediate = FK(ip, k1)
    Switch = InterMediate[4:] + InterMediate[:4]
    FinalResult = FK(Switch, k2)
    EncryptionAns = getPermute(FinalResult, 'IPIN')
    return EncryptionAns

def getDecryption(ip,k1,k2):
    InterMediate = FK(ip, k2)
    Switch = InterMediate[4:] + InterMediate[:4]
    FinalResult = FK(Switch, k1)
    EncryptionAns = getPermute(FinalResult, 'IPIN')
    return EncryptionAns

def getKey(key):
    p10 = getPermute(key, 'P10')
    left5 = p10[:5]
    right5 = p10[5:]

    k1 = getPermute((leftShift(left5) + leftShift(right5)), 'P8')
    k2 = getPermute(leftShift(leftShift(left5)) + leftShift(leftShift(right5)), 'P8')
    return k1,k2

if __name__ == "__main__":
    print('Enter plain text: ',end='')
    plainText = [int(i) for i in input()]
    print(f"Plaintext: {plainText}")

    print('\nEnter Cipher text: ',end='')
    cipherText = [int(i) for i in input()]

    import itertools
    keylist = list(map(list, itertools.product([0, 1], repeat=10)))
    # print(*lst,sep="\n")

    pairs = []
    for i in keylist:
        for j in keylist:
            ip = getPermute(plainText, 'IP')
            k1,k2 = getKey(i)
            IREncryption = getEncryption(ip, k1, k2)
            ip = getPermute(cipherText, 'IP')
            k1,k2 = getKey(j)
            IRDecryption = getDecryption(ip, k1, k2)

            if IREncryption == IRDecryption :
                print([i,j])
                sys.exit()