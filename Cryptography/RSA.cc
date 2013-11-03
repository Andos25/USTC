#include <cstdlib>
#include "RSA.h"

long random(long start, long end)
{
    return start+(end-start)*rand()/(RAND_MAX + 1.0);
}

long random_oddprime(long start, long end)
{
    for(long i = end; end != start; --i)
    {
        if(Miller_Rabin(i, 100))
        {
            return i;
        }
    }
}

long modular_exp(long a,long b,long n)//d≡a^b mod n
{
    long d=1;
    long t=a;
    while(b>0)
    {
      if(b%2==1)
       d=(d*t)%n;
      
      b=b/2;
      t=(t*t)%n;    
    } 
  return d;   
}   

void power(unsigned long a,unsigned long p,unsigned long n,unsigned long &result,bool &composite)
//计算 a^p mod n,并实施对n的二次探测
{
     unsigned long x;
     if(p==0)
        result=1;
     else
       {
           power(a,p/2,n,x,composite);//递归计算
           result=(x*x)%n;//二次探测
           if((result==1)&&(x!=1)&&(x!=n-1))
            composite=true;
           if((p%2)==1) //p是奇数
            result=(result*a)%n;
       }   
 }

 bool Miller_Rabin(unsigned long n,unsigned int k)
 //重复k次调用
 {
     unsigned long a,result;
     bool composite=false;
     srand(time(0));
     for(int i=1;i<=k;i++)
     {
        a=random(2, n-2);
        power(a,n-1,n,result,composite);
        if(composite||(result!=1))  return false;
     }
     return true;
 }

unsigned long gcd(unsigned long a, unsigned long b)
{
    unsigned long r;
    if(a < b)
    {
        int temp = b;
        b = a;
        a = temp;
    }
     while(true)
    {
        if(b == 0)
            return a;
        else
        {
            r = a % b;
            a = b;
            b = r;
        }
    }
}

unsigned long expand_gcd(unsigned long m, unsigned b)
{
    unsigned long a1 = 1, a2 = 0, a3 = m, b1 = 0, b2 = 1, b3 = b;
    unsigned long q, t1, t2, t3;
    while(true)
    {
        if(b3 == 1)
            return b2;
        if(b3 == 0)
            return b3;
        q = (long)a3 / b3;
        t1 = a1 - q*b1; t2 = a2 - q*b2; t3 = a3 - q*b3;
        a1 = b1; a2 = b2; a3 = b3;
        b1 = t1; b2 = t2; b3 = t3;
    }   
}

unsigned long generate_key(unsigned long &e, unsigned long &d, unsigned long &n)
{
    long p = random_oddprime(10000, 30000);
    long q = random_oddprime(10000, p-1);
    long n1 = (p-1)*(q-1);
    n = p*q;
    cout<<"n1:"<<n1<<endl;
    for(e=2; e!=n1; ++e)
    {
        if(gcd(e, n1) == 1)
        {
             d = expand_gcd(n1, e);
             if(e*d%n1 == 1)
                 break;
        }
    
    
    }
}

vector<string> encrypt(string plaintext, unsigned long e, unsigned long n)
{
    int s;
    string c;
    vector<string> ciphertext;
    for(string::size_type i=0; i!=plaintext.size(); ++i)
    {
        stringstream ss;
        s = (int)plaintext[i];
        s = modular_exp(s, e, n);
        ss << hex << s;
        ss >> c;
        ciphertext.push_back(c);
    }
    return ciphertext;
}

string decrypt(vector<string> ciphertext, unsigned long d, unsigned long n)
{
   int s;
   string c;
   string plaintext;
   for(vector<string>::size_type i=0; i!=ciphertext.size(); ++i)
   {
       stringstream ss;
       ss << hex <<ciphertext[i];
       ss >> s;
       s = modular_exp(s, d, n);
       plaintext += (char)s;
   }
   return plaintext;
}
