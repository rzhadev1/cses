#include <iostream>
#include <vector>

int main() {
	int n;
	std::cin >> n;
	
	int buf;
	long long total = 1;
	long long real = 1;
	for(int i = 1; i <= n; i++) {
		real += i;
	}

	for(int i = 0; i < n - 1; i++) {
		std::cin >> buf;
		total += buf;
	}
	
	int missing = real - total;
	std::cout << missing << std::endl;
	return 0;
}
