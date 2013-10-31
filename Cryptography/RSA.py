#!/usr/bin/env python
#coding = utf-8

#create by Andos he
#SA13226158
#email: h.chujieandos@gmail.com

import math
import random

def test(a, q, k, n):
    if a*q % n == 1:
        return False
    for j in range(k):
        if math.pow(a, math.pow(2, j)*q) % n == (n - 1):
            return False
    return True

def is_prime(n, confidence = 4):
    if n % 2 == 0 and n != 2:return False
    if n == 2:return True
    n1 = n - 1
    for q in range(1, n/2+1, 2):
        if not (n1 % q):
            k = math.log(n1/q, 2)
            if int(k) == k and k > 0:
                k = int(k)
                break
            else:
                continue

    count = 0
    
    for x in range(confidence):
        # a = random.randint(2, n1-1)
        a = 10
        print a, q, k, n
        if test(a, q, k, n):
            print "ok"
            return False
    return True

if __name__ == '__main__':
    print is_prime(5)