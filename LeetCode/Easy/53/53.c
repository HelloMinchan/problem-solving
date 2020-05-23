int maxSubArray(int* nums, int numsSize){
    int *table = (int *)malloc(sizeof(int)*numsSize);	//DP table set
    int max = 0;    //최대 합 저장 변수

    for(int i=0;i<numsSize;i++) {
	max = 0;
	if(nums[i]<=0)	//시작값이 음수라면 table에 그냥 저장후 패스
	    table[i]=nums[i];
	else {
	    max = table[i] = nums[i];

	    //뒤의 값들을 더해가며 시작값보다 큰 값이 있는지 탐색
	    for(int j=i+1;j<numsSize;j++) {
		max += nums[j];
		//table에 저장되어있던 값과 비교해 크다면 저장
		if(max > table[i])
		    table[i] = max;
	    }
	}
    }

    //table에서 최대 합을 찾아 저장
    max = -2147483648;
    for(int i=0;i<numsSize;i++) {
	if(max < table[i])
	    max = table[i];
    }

    return max;
}
