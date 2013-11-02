#include <iostream>
#include <ctime>
#include <cstdlib>
#include "RSA.h"

using namespace std;

long random(long start, long end)
{
    return start+(end-start)*rand()/(RAND_MAX + 1.0);
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

int main(int argc, char const *argv[])
 {
     /* code */
    cout<<Miller_Rabin(102840519238013, 100)<<endl;
    return 0;
 }
