#include <iostream>
#include <string.h>
#include <algorithm>
#include <list>
#include <stdio.h>
#include <fstream>
#include <time.h>
#include <fstream>
#include <chrono>
#include <vector>
const int V = 700;
using namespace std;

chrono::steady_clock::time_point t0;
bool did_timeout = false;
int t_max = 5*60*1000;

bool contains(vector<int> &collection, int element) {
    for (auto test : collection)
        if (test == element )
            return true;
    return false;
}

bool hamiltonian_cycle_dfs(int v, vector<int> &visited) {
    auto tl = chrono::steady_clock::now( );
    auto dt = chrono::duration_cast<std::chrono::milliseconds>(tl - t0).count();

    if (dt >= t_max) {
        did_timeout = true;
        return false;
    }
}

void printSolution(int path[]);

bool isSafe(int v, bool graph[V][V], int path[], int pos)
{
    if (graph [ path[pos-1] ][ v ] == 0)
        return false;

    for (int i = 0; i < pos; i++)
        if (path[i] == v)
            return false;

    return true;
}

bool hamCycleUtil(bool graph[V][V], int path[], int pos)
{
    if (pos == V)
    {
        if ( graph[ path[pos-1] ][ path[0] ] == 1 )
           return true;
        else
          return false;
    }

    for (int v = 1; v < V; v++)
    {

        if (isSafe(v, graph, path, pos))
        {
            path[pos] = v;
            if (hamCycleUtil (graph, path, pos+1) == true)
                return true;
            path[pos] = -1;
        }
    }

    return false;
}

bool hamCycle(bool graph[V][V])
{
    int *path = new int[V];
    for (int i = 0; i < V; i++)
        path[i] = -1;

    path[0] = 0;
    if ( hamCycleUtil(graph, path, 1) == false )
    {
        printf("\nNO");
        return false;
    }

    printSolution(path);
    return true;
}

void printSolution(int path[])
{
    printf ("YES\n");
    //for (int i = 0; i < V; i++)
        //printf(" %d ", path[i]);

    //printf(" %d ", path[0]);
    //printf("\n");
}

int main()
{
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/A&DS I/A&DS Report 4/HC-700-0.9.txt", "r");
	int i,j;
   bool graph1[V][V];
   for(i=0;i<V;i++)
  		for(j=0;j<V;j++)
   			graph1[i][j]=0;

	char line[100], v1[100], v2[100];
    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s", v1, v2);
        graph1[atoi(v1)][atoi(v2)] = 1;
    }
    float time = 0;
    for(int i = 0; i < 10; i++){
    const clock_t begin_time2 = clock();
    hamCycle(graph1);
    time += float( clock () - begin_time2 ) /  CLOCKS_PER_SEC;
    }
    cout << float(time/10);
    return 0;
}
