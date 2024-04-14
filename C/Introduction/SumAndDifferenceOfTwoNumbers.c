#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n1, m1;
    float n2,m2;
	scanf("%d %d", &n1, &m1);
    scanf("%f %f", &n2, &m2);
    
    if((n1<0) || (n1 > pow(10, 4))){
        return 0;
    }
    if((m1<0) || (m1 > pow(10, 4))){
        return 0;
    }
    if((n2<0) || (n2 > pow(10, 4))){
        return 0;
    }
    if((m2<0) || (m2 > pow(10, 4))){
        return 0;
    }
    
    printf("%d %d\n", n1+m1, n1-m1); 
    printf("%.1f %.1f", n2+m2, n2-m2);
    
    return 0;
}