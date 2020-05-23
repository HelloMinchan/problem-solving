#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int arr[3] = {0,};

    for(int i=0;i<3;i++)
	scanf("%d", &arr[i]);

    for(int i=0;i<3;i++)
	for(int j=0;j<3-1-i;j++)
	    if(arr[j]>arr[j+1])
		swap(&arr[j], &arr[j+1]);

    for(int i=0;i<3;i++)
	printf("%d ", arr[i]);

    return 0;
}
