#include <stdio.h>
#include <math.h>

int main()
{
float	x;
float	y;

for ( x=-10.0 ; x <= 100.0 ; x=x+3 )
	{
	if ( x >= 0){
	 y = sqrt(x); 
	printf("the value of %f is %f\n" , x, y);}

}
}
