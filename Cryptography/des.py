#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

from functools import partial 

hex_dict = {  
    '0':'0000','1':'0001','2':'0010','3':'0011',  
    '4':'0100','5':'0101','6':'0110','7':'0111',  
    '8':'1000','9':'1001','a':'1010','b':'1011',  
    'c':'1100','d':'1101','e':'1110','f':'1111',  
    ' ':'0000'  
}
ip_box = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 26, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
pc1_box = (
    57, 49, 41, 33, 25, 17,  9,
    1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
)
pc2_box = (
    14, 17, 11, 24, 1, 5, 3, 28,  
    15, 6, 21, 10, 23, 19, 12, 4,  
    26, 8, 16, 7, 27, 20, 13, 2,  
    41, 52, 31, 37, 47, 55, 30, 40,  
    51, 45, 33, 48, 44, 49, 39, 56,  
    34, 53, 46, 42, 50, 36, 29, 32,  
)
e_box = (
    32,  1,  2,  3,  4,  5,
    4 ,  5,  6,  7,  8,  9,
    8 ,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)

#transform to binary
trans_bin = partial(lambda hex_dict, text: ''.join(hex_dict[i] for i in ''.join(str(ord(w)) for w in text)), hex_dict)
#rotate left function
ro_left = lambda count, text: text[count:]+text[:count]
#xor function
xor = lambda string1, string2: ''.join(str(int(string1[i])^int(string2[i])) for i in range(string))
#common replacement function
replacement = lambda box, text: ''.join(text[i-1] for i in box)
#pc-1 replacement function
pc1_replacement = partial(replacement, pc1_box)
#pc-2 replacement function
pc2_replacement = partial(replacement, pc2_box)
#ip replacement function
ip_replacement = partial(replacement, ip_box)
#expand replacement function
expand_replacement = partial(replacement, e_box)

def round(text, key):
    text_R = text[]


def encrypt(plaintext, key):
    plaintext = trans_bin(plaintext)
    plaintext += '0'*(64-abs(len(plaintext)%64)) #digital fill
    for i in range(0, len(plaintext), 64):
        string = plaintext[i:i+64]
        string = ip_replacement(string)
        # for j in range(16)

if __name__ == '__main__':
    s = "密"
    encrypt(s, 1234)
    # print (trans_bin(s))
    # to_bin(s)