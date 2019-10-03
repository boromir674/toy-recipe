#include <iostream>
//# #include <string>
#include <string.h>
#include <sstream>
#include <iostream>
#include <cstring>
using namespace std;

int addition (int a, int b) {
  return a + b;
}

int stringToInteger(string NumberAsString)
{
	int NumberAsInteger;
	stringstream ss;
	ss << NumberAsString;
	ss >> NumberAsInteger;
	return NumberAsInteger;
}


int main(int argc, char** argv)
{
//  cout << "You have entered " << argc
//       << " arguments:" << "\n";

//  for (int i = 0; i < argc; ++i)
//    cout << argv[i] << "\n";

  int res = addition (stringToInteger(argv[1]), stringToInteger(argv[2]));
  cout << res;
//  cout << res  << endl;
  return 0;
}
