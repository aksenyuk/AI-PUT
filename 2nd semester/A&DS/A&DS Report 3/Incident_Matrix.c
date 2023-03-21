#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>
#define V 501
#define E (long int)(0.6 * (V * (V - 1)) / 2)

void init(int *arr)
{
    int i,j;
    for(i = 0; i < V; i++)
        for(j = 0; j < E; j++)
            arr[i * E + j] = 0;
}

void addEdge(int *arr, int v1, int v2, int place){
     arr[v1 * E + place] = 1;
     arr[v2 * E + place] = 1;
}

void printAdjMatrix(int *arr)
{
     int i, j;

     for(i = 0; i < V; i++)
     {
         for(j = 0; j < E; j++)
         {
             printf("%d ", arr[i * E + j]);
         }
         printf("\n");
     }
}

int search(int *arr, int a, int b){
    for(int i = 0; i < E; i++)
        if(arr[a * E + i] == 1 && arr[b * E + i] == 1)
            return 1;
    return 0;
}



int main()
{
    srand(time(0));
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/input edges.txt", "r");
    char line[100], v1[100], v2[100];
    int counter=0;

    int *arr = (int *)malloc(V * E * sizeof(int));

    //init(arr);

    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s", v1, v2);
        addEdge(arr, atoi(v1), atoi(v2), counter);
        counter++;;
    }

    clock_t tic = clock();
    int a = rand()%V, b = rand()%V;
    printf("%d\n", search(arr, a, b));
    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    free(arr);

    fclose(input_file);
    return 0;
}
