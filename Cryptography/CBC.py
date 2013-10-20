#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

import des

def encrypt(plaintext, key, IV):
    plaintext += ' ' * ((8-len(plaintext)%8)%8)
    plaintext = des.trans_bin(plaintext)
    key = des.trans_bin(key)
    IV = des.trans_bin(IV)[:64]
    if len(key) < 64 or len(IV) < 64:
        print "the length of key or IV is too short, at least 64, process will be stoped, please change and restart"
        return
    keylist = des.getkeylist(key)
    new_text = str()
    for i in range(0, len(plaintext), 64):
        string = plaintext[i:i+64]
        string = des.xor(string, IV)      #IV xor with plaintext block
        string = des.address_block(string, keylist)
        IV = des.ip1_replacement(string[32:]+string[:32])
        new_text += IV
    ciphertext = des.bin_trans_hex(new_text)
    return ciphertext

def decrypt(ciphertext, key, IV):
    key = des.trans_bin(key)
    ciphertext = des.hex_trans_bin(ciphertext)
    IV = des.trans_bin(IV)[:64]
    if len(key) < 64 or len(IV) < 64:
        print "the length of key or IV is too short, at least 64, process will be stoped, please change and restart"
        return
    keylist = des.getkeylist(key)
    keylist = keylist[::-1]
    new_text = str()
    for i in range(0, len(ciphertext), 64):
        cipher = ciphertext[i:i+64]
        string = des.address_block(cipher, keylist)
        string = des.ip1_replacement(string[32:]+string[:32])
        new_text += des.xor(string, IV)  #IV xor with cipher block
        IV = cipher
    plaintext = des.to_chr(new_text)
    return plaintext


if __name__ == '__main__':
    s = "我是明文aajaldjlak*!)@(#&%)!@#(*(!)@"
    key = '我就(^_^)是密钥'
    IV = "2j1ljdflaksjdlaksd"
    ciphertext = encrypt(s, key, IV)
    print ciphertext
    plaintext = decrypt(ciphertext, key, IV)
    print plaintext
