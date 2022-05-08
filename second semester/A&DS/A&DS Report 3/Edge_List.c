#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>
#define V 501
#define E (long int)(0.6 * (V * (V - 1)) / 2)

int search(int *arr, int a, int b){
    for(int i = 0; i < E; i++)
        if((arr[i * 2 + 0] == a && arr[i * 2 + 1] == b) || (arr[i * 2 + 0] == b && arr[i * 2 + 1] == a))
            return 1;
    return 0;
}


int main()
{
    srand(time(0));
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/input edges.txt", "r");
    char line[100], v1[100], v2[100];
    int *arr = (int *)malloc(E * 2 * sizeof(int));
    int idx=0;

    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s", v1, v2);
        arr[idx * 2 + 0] = atoi(v1);
        arr[idx * 2 + 1] = atoi(v2);
        idx++;
    }

    int a = rand()%V, b = rand()%V;
    clock_t tic = clock();
    printf("%d\n", search(arr, a, b));
    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);


    free(arr);

    fclose(input_file);

    return 0;
}
