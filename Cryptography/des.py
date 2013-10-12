#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

from functools import partial 
from Box import *

shift_digital = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)
#transform to binary
trans_bin = partial(lambda hex_dict, text: ''.join(hex_dict[i] for i in ''.join('%2x'%(ord(w)) for w in text)), hex_dict)
#binary transform to hex , string type 
bin_trans_hex = lambda string: '0'*((4-len('%16x' % int(string, 2))%4)%4)+'%16x' % int(string, 2)
#hex transform to binary , string type
hex_trans_bin = partial(lambda hex_dict, string: ''.join(hex_dict[i] for i in string), hex_dict)
#hex with string type transform to chr
string_trans_chr = lambda string: ''.join(chr(int(string[i:i+2], 16)) for i in range(0, len(string), 2))
#rotate left function
ro_left = lambda count, text: text[count:]+text[:count]
#xor function
xor = lambda string1, string2: ''.join(str(int(string1[i])^int(string2[i])) for i in range(len(string1)))
#common replacement function
replacement = lambda box, text: ''.join(text[i-1] for i in box)
#pc-1 replacement function
pc1_replacement = partial(replacement, pc1_box)
#pc-2 replacement function
pc2_replacement = partial(replacement, pc2_box)
#ip replacement function
ip_replacement = partial(replacement, ip_box)
#expand replacement function
e_replacement = partial(replacement, e_box)
#S-box choice replacement
s_replacement = partial(lambda s_box, hex_dict, string: ''.join(hex_dict['%x'%(s_box[i][int(string[i*6]+string[i*6+5], 2)*16 + int(string[i*6+1:i*6+5], 2)])] for i in range(8)), s_box, hex_dict)
#p replacement
p_replacement = partial(replacement, p_box)
#ip-1 replacement
ip1_replacement = partial(replacement, ip1_box)
#rotate left for key
ro_left_key = partial(lambda shift_digital, roundcount, key: ro_left(shift_digital[roundcount], key[:28])+ro_left(shift_digital[roundcount], key[28:]) ,shift_digital)
#get key list
addresskey = partial( lambda shiftlist, pc2_replacement, k: map(pc2_replacement,  
    (k[shiftlist[i]:28]+k[0:shiftlist[i]] + k[shiftlist[i]+28:56]+k[28:shiftlist[i]+28] for i in range(16)))  
    , shift_digital, pc2_replacement)  
getkeylist = partial( lambda pc1_replacement, shiftlist, k: shiftlist(pc1_replacement(k)), pc1_replacement, addresskey)
#transform result to ascii
to_chr = partial( lambda string: ''.join(chr(int(string[i:i+8], 2)) for i in range(0, len(string), 8)))

def round(text, key):
    R = text[32:]
    L = text[:32]
    R = e_replacement(R)
    R = xor(R, key)
    R = s_replacement(R)
    R = p_replacement(R)
    R = xor(R, L)
    return text[32:]+R

def address_block(text, keylist):
    new_text = str()
    for i in range(0, len(text), 64):
        string = text[i:i+64]
        string = ip_replacement(string)
        for j in range(16):
            string = round(string, keylist[j])
        new_text += ip1_replacement(string[32:]+string[:32])
    return new_text

def encrypt(plaintext, key):
    plaintext += ' ' * ((8-len(plaintext)%8)%8)
    plaintext = trans_bin(plaintext)
    key = trans_bin(key)
    if len(key) < 64:
        print "the length of key is too short, at least 64, process will be stoped, please change and restart"
        return
    keylist = getkeylist(key)
    ciphertext = address_block(plaintext, keylist)
    ciphertext = bin_trans_hex(ciphertext)
    return ciphertext

def decryption(ciphertext, key):
    key = trans_bin(key)
    ciphertext = hex_trans_bin(ciphertext)
    keylist = getkeylist(key)
    keylist = keylist[::-1]
    plaintext = address_block(ciphertext, keylist)
    plaintext = to_chr(plaintext)
    return plaintext

if __name__ == '__main__':
    s = "我是明文aajaldjlak*!)@(#&%)!@#(*(!)@"
    key = '我就(^_^)是密钥'
    ciphertext = encrypt(s, key)
    print ciphertext
    plaintext = decryption(ciphertext, key)
    print plaintext
