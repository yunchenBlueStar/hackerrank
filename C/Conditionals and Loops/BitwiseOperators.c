#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int andMaxVal, orMaxVal, xorMaxVal;
  andMaxVal = orMaxVal = xorMaxVal = 0;
  
  for(int i = 1; i < n; i++) {
      for (int j = i+1; j <= n; j++){
          andMaxVal = ( ((i & j) > andMaxVal) && ((i & j) < k)) ? (i & j) : andMaxVal;
          orMaxVal = ( ((i | j) > orMaxVal) && ((i | j) < k)) ? (i | j) : orMaxVal;
          xorMaxVal = ( ((i ^ j) > xorMaxVal) && ((i ^ j) < k)) ? (i ^ j) : xorMaxVal;
      }
  }
  printf("%d\n", andMaxVal);
  printf("%d\n", orMaxVal);
  printf("%d\n", xorMaxVal);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
