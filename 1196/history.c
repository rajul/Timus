#include <stdio.h>

int prof_nums[15001];
int n, m;
int key;

int binary_search() 
{
	int l = 0;
	int h = n - 1;
	int mid;

	while (l <= h) {
		mid = (l + h) / 2;

		if (prof_nums[mid] == key)
			return mid;
		else if (prof_nums[mid] < key) 
			l = mid + 1;
		else
			h = mid - 1;
	}

	return -1;
}

int main(int argc, char *argv[]) 
{
	int i, t, count = 0;
	
	scanf("%d", &n);

	for(i=0; i<n; i++)
		scanf("%d", &prof_nums[i]);

	scanf("%d", &m);

	for(i=0; i<m; i++) {
		scanf("%d", &key);

		t = binary_search();

		if (t != -1)
			count++;
	}

	printf("%d\n", count);


	return 0;
}
