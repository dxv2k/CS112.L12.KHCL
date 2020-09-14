#include <iostream>
#include<algorithm>
using namespace std;
//y tuong thuat toan
//ta bat dau tu dau mang
//p va q ban dau se la 0
//su dung mot bien check de kiem tra lai suat cua cac tram thu phi tu p den q
//tai vi tri a[i] neu tong lai suat be hon lai suat tai vi tri a[i thi ta se khong lay doan tu p den q chua tram thu phi a[i] nay => p = i + 1
//nguoc lai tuc lai suat khong bi lo thi ta se lay luon tram thu phi nay => q = i

int main()
{
    int n;
    cout << "nhap so nguyen n (1<= n <= 10^16 )" << endl;
    cin >> n;
    int a[100000];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int p = 0;
    int q = 0;

    int check = a[0];
    int kq = a[0];

    for (int i = 0; i < n; i++)
    {
        //neu tai vi tri a[i] ma tong lai suat lai nho hon lai suat thu duoc thi t se bo qua a[i] tuc gia tri cua p = i + 1
        if (a[i] >= check + a[i])
        {
            check = a[i];
            p = i + 1;
        }
        //nguoc lai thi q se dc gan bang vi tri cua i
        else
        {
            check = check + a[i];
            q = i;
        }

        kq = max(check, kq);

    }

    cout << p << " " << q << " " << kq << endl;

    return 0;
}