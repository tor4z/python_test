#include <stdio.h>


const char* filename = "test.bin";


int main()
{
    char c;
    int r = 0;
    int i=0;

    FILE *fp = fopen(filename, "rb");
    if(fp == NULL)
        fprintf(stderr, "Can not open %s", filename);

    while((fread(&c, 1, 1, fp))){   
        r |= c;
        r = r<<(8*(1-i));
        i++;
    }
    printf("%x\n", r);
    printf("%d\n", r);

    fclose(fp);
    return 0;
}