#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

#this is a example to encrypt image
from des import *

def encrypt_img(key, input, output):
    content = open(input, 'rb').read()
    ciphercontent = encrypt(content, key)
    f = open(output, 'wb')
    f.write(ciphercontent)
    f.close()

def decryption_img(key, input, output):
    content = open(input, 'rb').read()
    plaincontent = decryption(content, key)
    f = open(output, 'wb')
    f.write(plaincontent)
    f.close()

if __name__ == '__main__':
    key = "!@#)@(*&)@!(#*!@!*@()$*DasID"
    encrypt_img(key, 'plain.jpg', 'cipher.jpg')
    decryption_img(key, 'cipher.jpg', 'plain1.jpg')