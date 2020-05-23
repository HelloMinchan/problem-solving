#include <stdio.h>

int bucket[10001];

int main() {
    int N = 0;
    int num = 0;

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
	    scanf("%d", &num);
	    bucket[num]++;
    }

    for (int i = 1; i <= 10000; i++) {
	    for (int j = 0; j < bucket[i]; j++) {
	        printf("%d\n", i);
	    }
    }

    return 0;
}
