/*************************************************************************
	> File Name: RSA.h
	> Author: Andos he 
	> Mail: h.chujieandos@gmail.com 
	> Created Time: 2013年11月02日 星期六 11时00分41秒
 ************************************************************************/

long random(long start, long end);
long modular_exp(long a, long b, long n);
void power(unsigned long a, unsigned long p, unsigned long n, unsigned long &result, bool &composite);
bool Miller_Rabin(unsigned long n, unsigned int k);
