#include <stdio.h>

int main(void) {
FILE *fptr;
  fptr= fopen("xnyn.dat","w");
  double x[6]= {1,2,3,4,2,1};
  double y[30];
  int k=20;
  y[0]=x[0];
  y[1] = -0.5*y[0]+x[1];
  for(int n=2;n<k-1;n++)
    {
    if (n<6)
    {
      y[n] = -0.5*y[n-1]+x[n]+x[n-2];
    }
	  else if (n > 5  && n < 8)
      {
       y[n] = -0.5*y[n-1]+x[n-2];
      }
		 
	  else 
    {
      y[n] = -0.5*y[n-1];
    }
		  
    }
	 for (int i=0;i<k;i++)
     {
       fprintf(fptr,"%lf\n",y[i]);
     }
  fclose(fptr);
  
  return 0;
}
