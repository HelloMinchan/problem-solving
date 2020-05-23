int maxProfit(int* prices, int pricesSize) {
    int *table = (int *)malloc(sizeof(int)*pricesSize);	    //DP table set
    int max = 0;    //최댓값 저장 변수
    int max_index  = 0;	    //최댓값 인덱스 저장 변수

    //전체 날짜 만큼 반복
    for(int i=0;i<pricesSize;i++) {
	max=prices[i];
	table[i]=-max;	//주식을 날짜마다 무조건 사고 봄
	max_index = 0;

	//주식을 산 뒷 날에 혹시 팔아서 이득을 볼 수 있는지 탐색
	for(int j=i+1;j<pricesSize;j++) {
	    if(max<prices[j]) {
		max=prices[j];
		max_index=j;
	    }
	}
	//팔면 이득인 날에 주식을 팔기
	if(max_index!=0)
	    table[i]+=prices[max_index];   
    }

    //table에서 최대 이익인 날의 값 저장
    max = 0;
    for(int i=0;i<pricesSize;i++)
	if(max<table[i])
	    max=table[i];

    //최대 이익이 손해 였다면 0 저장
    if(max<0)
	max=0;

    return max;
}
