#include <stdio.h>
int main() {
    int num=0;
    int tot=0;
    scanf("%d",&tot);

    while(tot!=0) {
	if(tot>=50000) {
	    tot-=50000;
	    num++;
	}
	else if(tot>=10000&&tot<50000) {
	    tot-=10000;
	    num++;
	}
	else if(tot>=5000&&tot<10000) {
	    tot-=5000;
	    num++;
	}
	else if(tot>=1000&&tot<5000) {
	    tot-=1000;
	    num++;
	}
	else if(tot>=500&&tot<1000) {
	    tot-=500;
	    num++;
	}
	else if(tot>=100&&tot<500) {
	    tot-=100;
	    num++;
	}
	else if(tot>=50&&tot<500) {
	    tot-=50;
	    num++;
	}
	else {
	    tot-=10;
	    num++;
	}
    }
    printf("%d",num);
}
