#include <stdio.h>
int main() {
	unsigned int p1,p2,p3,j1,j2;
	unsigned int sp=0, sj=0;
	double price=0.0;
	
	scanf("%d%d%d%d%d",&p1,&p2,&p3,&j1,&j2);
	
	if (p1<p2) {
		sp=p1;
		if (sp>p3)
			sp=p3;
	}
	else {
		sp=p2;
		if (sp>p3)
			sp=p3;
	}
	
	if (j1<j2)
		sj=j1;
	else
		sj=j2;

	price = (double)((sp + sj) + ((double)(sp + sj) * 10/100));

	printf("%.1lf",price);
	return 0;
}
