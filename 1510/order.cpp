#include <stdio.h>
#include <map>

using namespace std;

int main() {
	map<int, int> counts;
	int max_count = 0;
	int max_num = 0;
	int i, n, t, x;

	scanf("%d", &n);

	for(i=0; i<n; i++)
	{
		scanf("%d", &t);

		x = counts[t] + 1;
		counts[t] = x;

		if(x > max_count)
		{
			max_count = x;
			max_num = t;
		}
	}

	printf("%d\n", max_num);
	return 0;
}