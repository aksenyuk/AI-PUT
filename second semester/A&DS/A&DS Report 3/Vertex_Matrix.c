#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>
#define V 501

void init(int *arr)
{
    int i,j;
    for(i = 0; i < V; i++)
        for(j = 0; j < V; j++)
            arr[i * V + j] = 0;
}

void addEdge(int *arr, int src, int dest)
{
     arr[src * V + dest] = 1;
     arr[dest * V + src] = 1;
}

void printAdjMatrix(int *arr)
{
     int i, j;

     for(i = 0; i < V; i++)
     {
         for(j = 0; j < V; j++)
         {
             printf("%d ", arr[i *  + j]);
         }
         printf("\n");
     }
}

int search(int *arr, int a, int b){
    if(arr[a * V + b] == 1 || arr[b * V + a] == 1)
        return 1;
    else
        return 0;
}



int main()
{
    srand(time(0));
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/input edges.txt", "r");
    char line[100], v1[100], v2[100];

    int *adjMatrix = (int *)malloc(V * V * sizeof(int));
    init(adjMatrix);

    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s", v1, v2);
        addEdge(adjMatrix, atoi(v1), atoi(v2));
    }

    int a = rand()%V, b = rand()%V;
    clock_t tic = clock();
    printf("%d\n", search(adjMatrix, a, b));
    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    free(adjMatrix);

    fclose(input_file);
    return 0;
}
