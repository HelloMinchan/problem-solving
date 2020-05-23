#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//살 날부터 팔 날까지 값을 1로 바꾸는 함수
void buy(int bought[], int first, int last) {
    for (int i = first; i < last; i++) {
	bought[i] = 1;
    }
    bought[last] = 0;
}

int main() {
    int T = 0;
    int N = 0;
    int max = 0;	//팔아야 되는 값
    int sell_day = 0;	//파는 날 인덱스
    int stuff = 0;	//산 물건의 수
    long profit = 0;	//이익 (이익의 최댓값이 int의 범위를 벗어나므로 long 타입 사용) 

    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
	profit = 0;
	stuff = 0;

	scanf("%d", &N);
	int *price = (int *)malloc(sizeof(int)*N);	//매매가 저장
	int *bought = (int *)malloc(sizeof(int)*N);	//산 날 저장
	memset(bought, 0, sizeof(bought));

	for (int i = 0; i < N; i++)
	    scanf("%d", &price[i]);

	//오늘 산다면 다음에 팔아서 이득이 되는 날이 있는지 찾기
	for (int i = 0; i < N - 1; i++) {
	    max = price[i];
	    //팔면 이득이 되는 날 찾기
	    for (int j = i + 1; j < N; j++) {
		if (max < price[j]) {
		    max = price[j];
		    sell_day = j;
		}
	    }
	    //오늘 사면 손해여서 사지 않았을때
	    if (max == price[i])
		continue;
	    //오늘 샀을때 팔 날까지 산 날 저장
	    else {
		buy(bought, i, sell_day);
		i = sell_day;
	    }
	}

	//총 이익 구하기
	for (int i = 0; i < N; i++) {
	    //이익에 물건을 산 날의 매매가 빼기
	    if (bought[i] == 1) {
		profit -= price[i];
		stuff++;
	    }
	    //이익에 물건을 판 날의 (매매가 * 물건의 수) 더하기
	    else {
		if (stuff != 0) {
		    profit += price[i] * stuff;
		    stuff = 0;
		}
	    }
	}

	free(price);
	free(bought);
	printf("#%d %ld\n", t + 1, profit);
    }

    return 0;
}
