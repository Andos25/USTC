#!/usr/bin/env python
#coding=utf-8

#create by Andos he
#SA13226158 of USTC
#email: h.chujieandos@gmail.com

import des


def init_S(key):
    S = [i for i in range(256)]
    T = [ord(key[i%len(key)]) for i in range(256)]
    j = 0
    for i in range(256):
        j = (j+S[i]+T[i])%256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keyflow():
     

