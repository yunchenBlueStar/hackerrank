#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d) {
    int maxVal = 0;
    
    if(a > maxVal) {
        maxVal = a;    
    }
    if(b > maxVal) {
        maxVal = b;    
    }
    if(c > maxVal) {
        maxVal = c;    
    }
    if(d > maxVal) {
        maxVal = d;    
    }
    
    return maxVal;
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

