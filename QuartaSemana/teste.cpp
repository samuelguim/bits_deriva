#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>

using namespace std;

int main(){
    char *a;
    char *b;

    do{
        cin >> a >> b;
        int x = strcmp(a, b);
        cout << x;
    } while (strcmp(a, b) != 0);

    return 0;   
}