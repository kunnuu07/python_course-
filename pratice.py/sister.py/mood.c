#include<stdio.h>
#include<string.h>

int main(){
char name[99];
printf("Your Name Dear: ");
scanf("%99[^\n]",name);

char mood[99];
printf("What Is Your Mood Right Now Dear \n %s happy or sad???\n ",name);
scanf("%s",mood);

char happy[] ="Happy";
char sad[] = "sad";

if (strcmp(mood,sad) == 0)
{
    char ans[99];
   printf("What Happend Dear %s, Why your felling Bad??\n \t answer me: ");
   scanf("%s",ans);
   printf("\nDon't Worry Dear %s Just smile And Fogot the Bad Things and Enjoy The Movement \n why you spoiling the Present Movement ?? \n",name);
}
else if (strcmp(mood,happy) == 0)
{
    printf("Thats Goog My Dear %s \n \t Keep Smiling ",name);
}
else
{
    printf("invalid Input Dear %s", name);
}

    return 0;
}