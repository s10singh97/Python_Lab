// Abstraction Property Implementation

#include<iostream>
using namespace std;
class A
{
    int i;
    public:
    void getdata()
    {
        i = 100;
        cout<<i;
    }
    void show();
};
void A::show()
{
    cout<<i;
}
int main(int argc, char const *argv[])
{
    A a;
    a.getdata();
    cout<<"char";
    a.show();
    return 0;
}
