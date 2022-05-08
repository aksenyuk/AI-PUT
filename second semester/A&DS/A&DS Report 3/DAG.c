#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>
#define n 501

//int n;
int adj[n][n];
void create_graph();

int queue[n], front = -1,rear = -1;
void insert_queue(int v);
int delete_queue();
int isEmpty_queue();

int indegree(int v);

int main()
{
        int i,v,count,topo_order[n],indeg[n];

        create_graph();

        clock_t tic = clock();
        for(i=0;i<n;i++)
        {
                indeg[i] = indegree(i);
                if( indeg[i] == 0 )
                        insert_queue(i);
        }

        count = 0;

        while(  !isEmpty_queue( ) && count < n )
        {
                v = delete_queue();
        topo_order[++count] = v;
                for(i=0; i<n; i++)
                {
                        if(adj[v][i] == 1)
                        {
                                adj[v][i] = 0;
                                indeg[i] = indeg[i]-1;
                                if(indeg[i] == 0)
                                        insert_queue(i);
                        }
                }
        }
        clock_t toc = clock();
        printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);
        //printf("\ntopological order:\n");
        //for(i=1; i<=count; i++)
                //printf( "%d ",topo_order[i] );
        //printf("\n");

        return 0;
}

void insert_queue(int vertex)
{
        if (rear == n-1)
                printf("\nQueue Overflow\n");
        else
        {
                if (front == -1)
                        front = 0;
                rear = rear+1;
                queue[rear] = vertex ;
        }
}

int isEmpty_queue()
{
        if(front == -1 || front > rear )
                return 1;
        else
                return 0;
}

int delete_queue()
{
        int del_item;
        if (front == -1 || front > rear)
        {
                printf("\nQueue Underflow\n");
                exit(1);
        }
        else
        {
                del_item = queue[front];
                front = front+1;
                return del_item;
        }
}

int indegree(int v)
{
        int i,in_deg = 0;
        for(i=0; i<n; i++)
                if(adj[i][v] == 1)
                        in_deg++;
        return in_deg;
}

void create_graph()
{
        int i,max_edges,origin,destin;
        FILE *input_file;
        input_file = fopen("C:/Users/1625203/Desktop/input edges.txt", "r");
        char line[100], v1[100], v2[100];

        max_edges = n*(n-1);

        while(fgets(line, sizeof line, input_file)){
            sscanf(line, "%s %s", v1, v2);
            adj[atoi(v1)][atoi(v2)] = 1;
        }
    fclose(input_file);
}
