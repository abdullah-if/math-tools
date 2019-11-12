#include<stdio.h>
#include<math.h> /*For trigonometric functions*/
/* #include<conio.h>   
  #include<windows.h>
  These headers are windows specific.
  If you compilpe on windows, then remove the comment symbol from the above headers and comment and # of lines marked with '#'. May warn for implicitly calling "system" */

int main()
{
	int func;
    double x, y;
    	
	
	/* #system("color 02");
    #SetConsoleTitle("Wide Range Trigonometry calculation- ); */
    printf("Wide Range Trigonometry calculation\n Choose Function From list:\n Trigonometry Functions: \n  1.tan\n  2.sin\n  3.cos\n Hyperbolic Trigonometry Functions: \n  4.tanh\n  5.sinh\n  6.cosh\n ");
    printf("Inverse Trigonometry Functions: \n  7.tan^-1\n  8.sin^-1\n  9.cos^-1\n Inverse Hyperbolic Functions: \n  a.tanh^-1\n  b.sinh^-1\n  c.cosh^-1\nPress e to exit\nType desired function number\n ");
    scanf("%x",&func); /*%x makes the input to be read as base-16*/

    if(func > 0 && func < 12 ) /* Loop , loop and more loops*/
    {
      printf("Value for x: ");
      scanf("%lf",&x);

       if (func == 1)
    {
    y = tan ( x  );
  printf ("The tangent of %f  is %f.\n", x, y );
  printf(" \n");

    }
    else if (func == 2)
    {
     y = sin ( x  );
  printf ("The sine of %f  is %f.\n", x, y );
  printf(" \n");
}
    else if (func == 3)
    {
     y = cos ( x  );
  printf ("The cosine of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 4)
    {
     y = tanh ( x  );
  printf ("The hyperbolic tangent of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 5)
    {
     y = sinh ( x  );
  printf ("The hyperbolic sine of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 6)
    {
     y = cosh ( x  );
  printf ("The hyperbolic cosine of %f  is %f.\n", x, y );
  printf(" \n");

    }
    else if (func == 7)
    {
     y = atan ( x  );
  printf ("The arctangent of %f  is %f.\n", x, y );
  printf(" \n");

    }
    else if (func == 8)
    {
    y = asin ( x  );
  printf ("The arcsine of %f  is %f.\n", x, y );
  printf(" \n");


    }
    else if (func == 9)
    {
    y = acos( x  );
  printf ("The arc-cosine of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 10)
    {
    y = atanh ( x  );
  printf ("The hyperbolic arctangent of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 11)
    {
    y = asinh ( x  );
  printf ("The hyperbolic arcsine of %f  is %f.\n", x, y );
  printf(" \n");

    }
     else if (func == 12)
    {
    y = acosh ( x  );
  printf ("The hyperbolic arc-cosine of %f  is %f.\n", x, y );
  printf(" \n");
    }
    printf("Press any key to returm to main menu");
      getchar();
      getchar();
	/* #system("pause");
	#system("cls"); use these instead of getchar()*/
    return main();
    }
    else if(func == 14) /*Home brewed quit function*/
    {
        return 0;
    }
   else
    {
        printf("ERROR!");
        printf(" \n");
        printf("Press any key to returm to main menu");
      getchar();
      getchar();
	  /* #system("pause");
	   #system("cls");*/
    return main();
    }
}




