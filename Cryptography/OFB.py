#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

import des

def encrypt(plaintext, key, IV, s_length):
    # plaintext += ' ' * ((8-len(plaintext)%8)%8)
    plaintext = des.trans_bin(plaintext)
    key = des.trans_bin(key)
    IV = des.trans_bin(IV)[:64]
    if len(key) < 64 or len(IV) < 64:
        print "the length of key or IV is too short, at least 64, process will be stoped, please change and restart"
        return
    keylist = des.getkeylist(key)
    new_text = str()
    for i in range(0, len(plaintext), s_length):
        string = plaintext[i:i+s_length]
        cipher = des.address_block(IV, keylist)
        cipher = des.ip1_replacement(cipher[32:]+cipher[:32])
        IV = IV[s_length:] + cipher[:s_length]
        cipher = des.xor(cipher[:s_length], string)
        new_text += cipher
        
    ciphertext = des.bin_trans_hex(new_text)
    return ciphertext

def decrypt(ciphertext, key, IV, s_length):
    key = des.trans_bin(key)
    ciphertext = des.hex_trans_bin(ciphertext)
    IV = des.trans_bin(IV)[:64]
    if len(key) < 64 or len(IV) < 64:
        print "the length of key or IV is too short, at least 64, process will be stoped, please change and restart"
        return
    keylist = des.getkeylist(key)
    # keylist = keylist[::-1]
    new_text = str()
    for i in range(0, len(ciphertext), s_length):
        cipher = ciphertext[i:i+s_length]
        plain = des.address_block(IV, keylist)
        plain = des.ip1_replacement(plain[32:]+plain[:32])
        IV = IV[s_length:] + plain[:s_length]
        new_text += des.xor(plain[:s_length], cipher)
    plaintext = des.to_chr(new_text)
    return plaintext

if __name__ == '__main__':
    s = "我是明文aajaldjlak*!)@(#&%)!@#(*(!)@"
    key = '我就(^_^)是密钥'
    IV = "2j1ljdflaksjdlaksd"
    ciphertext = encrypt(s, key, IV, 8)
    print ciphertext
    plaintext = decrypt(ciphertext, key, IV, 8)
    print plaintext
