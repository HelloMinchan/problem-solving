int rob(int* nums, int numsSize) {
    int *table = (int *)malloc(sizeof(int)*numsSize);	//DP table set
    int sum = 0;    //총 금액 저장 변수

    if(numsSize==0) //input으로 아무 것도 없는 배열 예외처리
	sum = 0;
    else if(numsSize==1)    //input으로 길이가 1인 배열 예외처리
	sum = nums[0];
    else {
	for(int i=0;i<numsSize;i++) {
	    if(i==0 || i==1)	//index가 0 혹은 1 이면 그대로 table에저장
		table[i]=nums[i];
	    else    // index가 0과 1이 아닐경우
		table[i]=nums[i]+table[i-2];
	    if(i>=3){	//만약 index가 3이상일 경우 전전집과 전전전집까지 강탈한 돈의 총액중 큰 금액 부터 이어서 강탈함
		if(table[i-2]>=table[i-3])
		    table[i]=nums[i]+table[i-2];
		else
		    table[i]=nums[i]+table[i-3];       
	    }
	}
	//table의 맨 마지막값과 마지막 직전 값중 큰 값이 털 수 있는 최대 금액임
	if(table[numsSize-2]>table[numsSize-1])
	    sum=table[numsSize-2];
	else
	    sum=table[numsSize-1];
    }

    free(table);
    return sum;
}
