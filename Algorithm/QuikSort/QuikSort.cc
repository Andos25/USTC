#include <iostream>
#include <time.h>
using namespace std;

template <typename T>
int Partition(T t[],int p,int r)
{
    T key = t[r], tmp;
    int i = p-1;
    for(int j=p; j<r; ++j)
    {
        if(t[j] < key)
        {
            ++i;
            tmp = t[j];
            t[j] = t[i];
            t[i] = tmp;
        }
    }
    t[r] = t[i+1];
    t[i+1] = key;
    return i+1;
}

template <typename T>
void QuikSort(T t[], int p, int r)
{
    if(p < r)
    {
        int q = Partition(t, p, r);
        QuikSort(t, p, q-1);
        QuikSort(t, q+1, r);
    }
}

int main()
{
    int t[10000];
    for(int i=0; i!=10000; ++i)
        t[i] = i;
    clock_t begin, end;
    double duration;
    begin = clock();
    QuikSort(t, 0, 9999);
    end = clock();
    duration = (double)(end - begin)/CLOCKS_PER_SEC; 
    for(int i=0; i!=10000; ++i )
        cout<<t[i]<<endl;
    cout<<"time:"<<duration<<endl;
}
