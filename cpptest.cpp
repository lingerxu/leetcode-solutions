#include <iostream>
using namespace std;

int main() 
{
    char sym;
    float n1;
    float n2;

    cout << "enter a symbol: ";
    cin >> sym;

    cout << "please enter the numbers: ";
    cin >> n1 >> n2;

    switch(sym)
    {
        case '+':
            cout << n1 << " + " << n2 << " = ";
            cout << n1+n2;
        
        case '-':
            cout << n1 << " - " << n2 << " = ";
            cout << n1-n2;
        
        case '*':
            cout << n1 << " * " << n2 << " = ";
            cout << n1*n2;
        
        case '/':
            cout << n1 << " / " << n2 << " = ";
            cout << n1/n2;
    }
    return 0;
}