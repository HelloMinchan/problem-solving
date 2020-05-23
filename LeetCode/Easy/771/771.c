int numJewelsInStones(char * J, char * S){
    int arr[52] ={0,};
    int n1 = strlen(S);
    int n2 = strlen(J);
    int num = 0;
    
    for(int i=0;i<n1;i++){
        if(S[i]>=65&&S[i]<=90)
            arr[S[i]-65] += 1;
        else
            arr[S[i]-71] += 1;
    }
    
    for(int i=0;i<n2;i++){
        if(J[i]>=65&&J[i]<=90)
            num += arr[J[i]-65];
        else
            num += arr[J[i]-71];
    }
    
    return num;
}
