#include <stdio.h>
int main() {
    int T = 0;
    scanf("%d", &T);
    int arr[10] = { 0, };
    int max[10000] = { 0, };
    int index = 0;

    for (int i = 0; i < T; i++) {
	for (int j = 0; j < 10; j++) {
	    scanf("%d", &arr[j]);

	    if (max[index] < arr[j])
		max[index] = arr[j];
	}
	index++;
    }

    for (int i = 0; i < index; i++) {
	printf("#%d %d\n", i + 1, max[i]);
    }
    return 0;
}
