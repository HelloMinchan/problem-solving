#include <stdio.h>
#include <stdlib.h>
#define SWAP(a, b) {a^=b, b^=a, a^=b;}

int main(void) {
    int N = 0, min = 0;
    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int)*N);

    for (int i = 0; i < N; i++)
	    scanf("%d", &arr[i]);

    for (int i = 0; i < N - 1; i++) {
	    min = i;
	    for (int j = i + 1; j < N; j++) {
	        if (arr[min] > arr[j])
		    min = j;
	    }
	    if(min != i)
	        SWAP(arr[i], arr[min]);
    }

    for (int i = 0; i < N; i++)
	    printf("%d\n", arr[i]);

    free(arr);
    return 0;
}
