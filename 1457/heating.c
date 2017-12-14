#include <stdio.h>

int main(int argc, char argv[])
{
	int n;
	int i, t, total;
	double avg;

	scanf("%d", &n);

	total = 0;
	avg = 0.0;

	for(i=0; i<n; i++)
	{
		scanf("%d", &t);
		total = total + t;
	}

	avg = (double)total / n;

	printf("%.6lf\n", avg);

	return 0;
}