#!/usr/bin/python
#--*-- coding: utf-8 --*--

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

import random

leftshift = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
S = (   #S1
        (14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,  
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,  
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,  
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13),  
        #S2  
        (15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,  
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,  
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,  
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9),  
        #S3  
        (10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,  
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,  
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,  
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12),  
        #S4  
        (7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,  
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,  
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,  
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14),  
        #S5  
        (2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,  
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,  
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,  
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3),  
        #S6  
        (12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,  
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,  
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,  
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13),  
        #S7  
        (4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,  
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,  
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,  
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12),  
        #S8  
        (13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,  
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,  
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,  
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11)
    )

def stringtobin(string):
    result = str()
    for i in string:
        result += str(bin(ord(i)))[2:]
    return result

def des_encrypt(inputfilepath, keyfilepath, outputfilepath):
    plaintext = stringtobin(open(inputfilepath).read())
    print plaintext
    count = len(plaintext)/64
    cipertext = str()
    for i in range(count):
        cipertext += encrypt(plaintext)
        plaintext = plaintext[64:]
    fillingstring = ''.join(random.sample('01', 64 - len(plaintext)))
    plaintext += fillingstring
    cipertext += encrypt(plaintext)
    f = open(outputfilepath, 'w')
    f.write(cipertext)
    f.close()

#about key
def replacement_choice1(key):
    matrix = (57, 49, 41, 33, 25, 17,  9,\
               1, 58, 50, 42, 34, 26, 18,\
              10,  2, 59, 51, 43, 35, 27,\
              19, 11,  3, 60, 52, 44, 36,\
              63, 55, 47, 39, 31, 23, 15,\
               7, 62, 54, 46, 38, 30, 22,\
              14,  6, 61, 53, 45, 37, 29,\
              21, 13,  5, 28, 20, 12,  4)
    new_key = str()
    for i in range(56):
        new_key += key[matrix[i-1]]
    return new_key

#about plaintext
def initialreplacement(plaintext_block):
    IPmatrix = (58, 50, 42, 34, 26, 18, 10, 2,\
                60, 52, 44, 36, 28, 20, 12, 4,\
                62, 54, 46, 38, 30, 22, 14, 6,\
                64, 56, 48, 40, 32, 24, 16, 8,\
                57, 49, 41, 33, 26, 17, 9,  1,\
                59, 51, 43, 35, 27, 19, 11, 3,\
                61, 53, 45, 37, 29, 21, 13, 5,\
                63, 55, 47, 39, 31, 23, 15, 7)
    new_plaintext_block = str()
    for i in range(64):
        new_plaintext_block += plaintext_block[IPmatrix[i-1]]
    return new_plaintext_block

def encrypt(plaintext):
    print initialreplacement(plaintext)

def round(new_plaintext_block, key, count):
    L = new_plaintext_block[:32]
    R = new_plaintext_block[32:]

def expand(Rstring):
    expandmatrix = (32,  1,  2,  3,  4,  5,\
                    4 ,  5,  6,  7,  8,  9,\
                    8 ,  9, 10, 11, 12, 13,\
                    12, 13, 14, 15, 16, 17,\
                    16, 17, 18, 19, 20, 21,\
                    20, 21, 22, 23, 24, 25,\
                    24, 25, 26, 27, 28, 29,\
                    28, 29, 30, 31, 32, 1)
    new_string = str()
    for i in range(32):
        new_string += Rstring[expandmatrix[i-1]]
    return new_string




if __name__ == '__main__':
    des_encrypt('test', 'key', 'output')
    # print open("test", "rb").read()
    # randomstring = ''.join(random.sample('01', 8))
    # print randomstring







