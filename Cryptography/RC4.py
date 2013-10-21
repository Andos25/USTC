#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

import des

single = (0,1,2,3,4,5,6,7,8,9)

def init_S(key):
    S = [i for i in range(256)]
    T = [ord(key[i%len(key)]) for i in range(256)]
    j = 0
    for i in range(256):
        j = (j+S[i]+T[i])%256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keyflow(i ,j, S):
    i = (i+1) % 256
    j = (j+S[i]) % 256
    S[i], S[j] = S[j], S[i]
    t = (S[i] + S[j]) % 256
    return S, t

def encrpyt(plaintext, key):
    S = init_S(key)
    ciphertext = str()
    i = int(0)
    j = int(0)
    for c in plaintext:
        S, t = generate_keyflow(i, j, S)
        cipher = ord(c)^S[t]
        if cipher in single:
            ciphertext += '0'
        ciphertext += '%x'%(cipher)
    return ciphertext

def decrypt(ciphertext, key):
    S = init_S(key)
    plaintext = str()
    i = int(0)
    j = int(0)
    for c in range(0, len(ciphertext), 2):
        plain = int(ciphertext[c:c+2], 16)
        S, t = generate_keyflow(i, j, S)
        plain = plain^S[t]
        plaintext += chr(plain)
    return plaintext
        
if __name__ == '__main__':
    key = "我就(^_^)是密钥"
    s = "我是明文aajaldjlak*!)@(#&%)!@#(*(!)@"
    ciphertext = encrpyt(s, key)
    print ciphertext
    plaintext = decrypt(ciphertext, key)
    print plaintext

     

