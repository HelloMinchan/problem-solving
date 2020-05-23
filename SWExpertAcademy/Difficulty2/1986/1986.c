#include <stdio.h>
#include <stdlib.h>

int main() {
    int t = 0;
    scanf("%d", &t);
    int *sum = (int *)malloc(sizeof(int)*t);
    int index = 0;
    int N = 0;

    for (int i = 0; i < t; i++) {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
	    if (i % 2 == 0)
		sum[index] -= i;
	    else
		sum[index] += i;
	}
	index++;
    }

    for (int i = 0; i < t; i++) {
	printf("#%d %d\n", i + 1, sum[i]);
    }

    free(sum);
    return 0;
}
