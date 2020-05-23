#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int n = 0;
    scanf("%d", &n);

    int *arr = (int *)malloc(sizeof(int)*n);

    for(int i=0;i<n;i++)
	scanf("%d", &arr[i]);

    for(int i=0;i<n;i++)
	for(int j=0;j<n-1-i;j++)
	    if(arr[j]<arr[j+1])
		swap(&arr[j], &arr[j+1]);

    for(int i=0;i<n;i++)
	printf("%d ", arr[i]);

    free(arr);

    return 0;
}
