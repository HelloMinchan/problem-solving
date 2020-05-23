#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    int num1 = *(int *)a;
    int num2 = *(int *)b;

    if (num1 < num2)
        return -1;
    
    if (num1 > num2)
        return 1;
    
    return 0;
}

int main()
{
    int n = 0;
    scanf("%d", &n);

    int *arr1 = (int *)malloc(sizeof(int)*n);
    int *arr2 = (int *)malloc(sizeof(int)*n);

    for(int i=0;i<n;i++) {
	scanf("%d", &arr1[i]);
	arr2[i] = arr1[i];
    }

    qsort(arr1, n, sizeof(int), compare);

    for (int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
	    if(arr2[i]==arr1[j])
		printf("%d ", j);
	}
    }

    free(arr1);
    free(arr2);

    return 0;
}
