#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    char s[1000];
    scanf("%s", s);
    
    for (int i = 0; i <= 9; i++) {
       int times = 0; 
       for (int j = 0; j < strlen(s); j++) {
           int val = (int) s[j] - 48;
           if(val == i) times++;    
       }
       printf("%d ", times);
    }
     
    return 0;
}
