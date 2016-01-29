#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<int> stack;

void pop() {
    if( !stack.empty() )
        stack.pop_back();
    if( stack.empty() ) {
        cout << "EMPTY" << endl;
    } else {
        cout << stack.back() << endl;
    }
}

void push( int a ) {
    cout << a << endl;
    stack.push_back( a );
}

void inc( int x, int d ) {
    for( int i = 0; i < x; ++i ) {
        stack[i] += d;
    }
    cout << stack.back() << endl;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int opNumber;
    string option;
    getline(cin, option);
	opNumber = stoi(option);
	
    
    stack.reserve(opNumber);
    string buf; 
    for (int i = 0; i < opNumber; ++i){
        getline(cin, option);
		cout << option << endl;
        stringstream ss(option);
       
        vector<string> token;
        while (ss >> buf) {
            token.push_back( buf );
        }
        if( token.size() == 1 && token[0] == "pop") {
            pop();
        } else if( token.size() == 2 && token[0] == "push" ) {
            push( stoi(token[1]) );
        } else if( token.size() == 3 && token[0] == "inc" ) {
            inc( stoi(token[1]), stoi(token[2]) );
        }
    }
    return 0;
}
