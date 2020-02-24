#include <stdio.h>
#include <stdlib.h>
#define SWAP(a, b) {a^=b, b^=a, a^=b;}

int main() {
    int N = 0;

    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++)
	scanf("%d", &arr[i]);

    for (int i = 0; i < N - 1; i++) {
	for (int j = 0; j < N - i - 1; j++) {
	    if (arr[j] > arr[j + 1])
		SWAP(arr[j], arr[j + 1]);
	}
    }

    for (int i = 0; i < N; i++)
	printf("%d\n", arr[i]);

    free(arr);
    return 0;
}
