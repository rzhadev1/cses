#include <iostream>
#include <string>
#include <limits>

using namespace std;
int max_len_substring(const char c, const string& s) {
	int curr_max = 0;
	int total_max = std::numeric_limits<int>::min();

	for(auto& character : s) {
		if(character == c) {
			curr_max++;
			total_max = max(curr_max, total_max);
		}
		else {
			total_max = max(curr_max, total_max);
			curr_max = 0;
		}
	}

	return total_max;
}

int main() {
	string s;
	getline(cin, s);
	int g = max_len_substring('G', s);
	int a = max_len_substring('A', s);
	int c = max_len_substring('C', s);
	int t = max_len_substring('T', s);
	
	cout << max(max(g,a), max(c,t)) << endl;
	return 0;
}
