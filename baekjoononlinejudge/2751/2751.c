#include <stdio.h>
#include <stdlib.h>

void merge(int *arr, int p, int q, int r) {
    int i = p;
    int j = q + 1;
    int t = 0;
    int *temp = (int *)malloc(sizeof(int) * (r-p+1));

    while (i <= q && j <= r) {
	    if (arr[i] <= arr[j])
	        temp[t++] = arr[i++];
	    else
	        temp[t++] = arr[j++];
    }
    while (i <= q)
	    temp[t++] = arr[i++];
    while (j <= r)
	    temp[t++] = arr[j++];
    i = p;
    t = 0;
    while (i <= r)
	    arr[i++] = temp[t++];

    free(temp);
}

void mergeSort(int *arr, int p, int r) {
    if (p < r) {
	int q = (p + r) / 2;
	    mergeSort(arr, p, q);
	    mergeSort(arr, q + 1, r);
	    merge(arr, p, q, r);
    }
}

int main() {
    int N = 0;

    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++)
	    scanf("%d", &arr[i]);

    mergeSort(arr, 0, N - 1);

    for (int i = 0; i < N; i++)
	    printf("%d\n", arr[i]);

    free(arr);
    return 0;
}
