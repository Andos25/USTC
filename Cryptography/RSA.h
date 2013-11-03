/*************************************************************************
	> File Name: RSA.h
	> Author: Andos he 
	> Mail: h.chujieandos@gmail.com 
	> Created Time: 2013年11月02日 星期六 11时00分41秒
 ************************************************************************/
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

long random(long start, long end);
long random_oddprime(long start, long end);
long modular_exp(long a, long b, long n);
void power(unsigned long a, unsigned long p, unsigned long n, unsigned long &result, bool &composite);
bool Miller_Rabin(unsigned long n, unsigned int k);
unsigned long gcd(unsigned long a, unsigned long b);
unsigned long expand_gcd(unsigned long m, unsigned b);
unsigned long generate_key(unsigned long &e, unsigned long &d, unsigned long &n);
string decrypt(vector<string> ciphertext, unsigned long d, unsigned long n);
vector<string> encrypt(string plaintext, unsigned long e, unsigned long n);

