#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int N = 0, min = 0, j = 0;
    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int)*N);

    for (int i = 0; i < N; i++)
	    scanf("%d", &arr[i]);

    for (int i = 1; i < N; i++) {
	    min = arr[i];
	    for (j = i - 1; j >= 0 && min < arr[j]; j--)
	        arr[j+1] = arr[j];
	    arr[j+1] = min;
    }

    for (int i = 0; i < N; i++)
	    printf("%d\n", arr[i]);

    free(arr);
    return 0;
}
