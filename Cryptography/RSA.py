#!/usr/bin/env python
#coding = utf-8

#create by Andos he
#SA13226158
#email: h.chujieandos@gmail.com

import math
import random

def test(a, q, k, n):
    if a*q % n == 1:
        print a*q, n
        return False
    for j in range(k):
        s = int(math.pow(2, j)*q)
        print a,s,n,n-1
        if modular_exp(a, s, n) == (n - 1):

            return False
    return True

def modular_exp(a, b, n): #a^b mod n
    d = 1
    t = a
    while b>0:
        if b % 2 == 1:
            d = (d * t) % n
        b /= 2
        t = (t * t) % n
    return d

def is_prime(n):
    if n == 2 or n == 5:return True
    if n % 2 == 0:return False
    n1 = n - 1
    for q in range(1, n/2+1, 2):
        if not (n1 % q):
            k = math.log(n1/q, 2)
            if int(k) == k and k > 0:
                k = int(k)
                break
            else:
                continue
    print "k", k
    for x in range(10):
        a = random.randint(2, n1-1)
        # a = 10
        if test(a, q, k, n):
            return False
    return True

# def generate_prime():


if __name__ == '__main__':
    print is_prime(9999999999999999)
