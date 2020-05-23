int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *twosum = (int *)malloc(sizeof(int)*2);
    int rest = 0;

    for(int i=0;i<numsSize-1;i++){
	rest = target-nums[i];
	for(int j=i+1;j<numsSize;j++){
	    if(nums[j]==rest){
		twosum[0]=i;
		twosum[1]=j;
		*returnSize = 2;
		return twosum;
	    }
	}
    }
    *returnSize = 0;
    return NULL;
}
