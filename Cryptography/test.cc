#include "RSA.h"

int main()
{
    unsigned long n,e,d;
    string decryption;
    string plaintext("Welcome to USTC");
    cout<<"plaintext is "<<plaintext<<endl;
    vector<string> ciphertext;
    generate_key(e, d, n);
    cout<<"e:"<<e<<"d:"<<d<<"n:"<<n<<endl;
    ciphertext = encrypt(plaintext, e, n);
    cout<<"ciphertext is ";
    for(vector<string>::size_type i=0; i!=ciphertext.size(); ++i)
        cout<<ciphertext[i];
    cout<<endl;
    decryption = decrypt(ciphertext, d, n);
    cout<<"decryption is "<<decryption<<endl;

}

