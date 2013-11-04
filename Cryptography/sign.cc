#include "RSA.h"

int main()
{
    unsigned long Ae, Ad, An;
    unsigned long Be, Bd, Bn;
    generate_key(Ae, Ad, An);
    generate_key(Be, Bd, Bn);
    string plaintext("Welcome to USTC");
    cout<<"the sign is :";
    vector<string> S = encrypt(plaintext, Ae, An);
    for(vector<string>::size_type i=0; i!=S.size(); ++i)
        cout<<S[i];
    cout<<endl;
    vector<string> ciphertext = encrypt(plaintext, Be, Bn);
    cout<<"ciphertext is :";
    for(vector<string>::size_type i=0; i!=ciphertext.size(); ++i)
        cout<<ciphertext[i];
    cout<<endl;
    string decryption = decrypt(ciphertext, Bd, Bn);
    cout<<"decryption is "<<decryption<<endl;
    string M = decrypt(S, Ad, An);
    if(M == plaintext)
        cout<<"签名检查成功"<<endl;
    else
        cout<<"签名检查失败"<<endl;

}

