#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    char* numberToStr[10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    if(a < 0 || a > b || b > pow(10, 3)) {
        return 0;  
    }
    
    for(int i = a; i <= b; i++) {
        if(i>=1 && i <= 9) {
            printf("%s\n", numberToStr[i-1]);
        } else if (i > 9) {
            if(i % 2 == 0 ) {
                    printf("even\n");
            } else {
                printf("odd\n");
            }
        }
    }
    
 
    
    return 0;
}

