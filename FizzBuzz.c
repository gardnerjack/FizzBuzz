#include <stdio.h>
int main(){char*s;for(int i=0;++i<101;){sprintf(s,"%d",i);puts(i%3?(i%5?s:"Buzz"):(i%5?"Fizz":"FizzBuzz"));}}
