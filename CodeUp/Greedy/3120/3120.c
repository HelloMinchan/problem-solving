#include <stdio.h>
int main() {
    int start = 0;
    int final = 0;
    int num = 0;

    scanf("%d%d",&start,&final);

    while(1) {
	if(final-start>0) {
	    if(final-start>=8)
		start+=10;
	    else if(final-start<8&&final-start>=3)
		start+=5;
	    else
		start+=1;

	    num++;
	}
	else if(final-start<0) {
	    if(final-start<=-8)
		start-=10;
	    else if(final-start>-8&&final-start<=-3)
		start-=5;
	    else
		start-=1;

	    num++;
	}
	else
	    break;
    }
    printf("%d",num);
}
