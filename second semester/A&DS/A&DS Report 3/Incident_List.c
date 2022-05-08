#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>
#define V 501
#define E (long int)(0.6 * (V * (V - 1)) / 2)

struct node {
  int vertex;
  struct node* next;
};

struct node* createNode(int v);

struct Graph {
  int numVertices;
  int* visited;

  // We need int** to store a two dimensional array.
  // Similary, we need struct node** to store an array of Linked lists
  struct node** adjLists;
};

// DFS algo
void DFS(struct Graph* graph, int vertex, int v2, int *check) {
    printf("%d %d \n", vertex, v2);
    if (vertex == v2) {*check = 1; return;}

  struct node* adjList = graph->adjLists[vertex];
  struct node* temp = adjList;

  graph->visited[vertex] = 1;
  printf("Visited %d \n", vertex);

  while (temp != NULL) {
    int connectedVertex = temp->vertex;

    if (graph->visited[connectedVertex] == 0) {
      DFS(graph, connectedVertex, v2, check);
    }
    temp = temp->next;
  }
}

// Create a node
struct node* createNode(int v) {
  struct node* newNode = malloc(sizeof(struct node));
  newNode->vertex = v;
  newNode->next = NULL;
  return newNode;
}

// Create graph
struct Graph* createGraph(int vertices) {
  struct Graph* graph = malloc(sizeof(struct Graph));
  graph->numVertices = vertices;

  graph->adjLists = malloc(vertices * sizeof(struct node*));

  graph->visited = malloc(vertices * sizeof(int));

  int i;
  for (i = 0; i < vertices; i++) {
    graph->adjLists[i] = NULL;
    graph->visited[i] = 0;
  }
  return graph;
}

// Add edge
void addEdge(struct Graph* graph, int src, int dest) {
  // Add edge from src to dest
  struct node* newNode = createNode(dest);
  newNode->next = graph->adjLists[src];
  graph->adjLists[src] = newNode;

  // Add edge from dest to src
  newNode = createNode(src);
  newNode->next = graph->adjLists[dest];
  graph->adjLists[dest] = newNode;
}

// Print the graph
void printGraph(struct Graph* graph) {
  int v;
  for (v = 0; v < graph->numVertices; v++) {
    struct node* temp = graph->adjLists[v];
    printf("\n Adjacency list of vertex %d\n ", v);
    while (temp) {
      printf("%d -> ", temp->vertex);
      temp = temp->next;
    }
    printf("\n");
  }
}

int main() {
    struct Graph* graph = createGraph(V);
    srand(time(0));
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/input edges.txt", "r");
    char line[100], v1[100], v2[100];
    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s", v1, v2);
        addEdge(graph, atoi(v1), atoi(v2));
    }

    int check=0;
    int a = rand()%V, b = rand()%V;
    clock_t tic = clock();
    DFS(graph, 1, 0, &check);
    printf("%d \n", check);
    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);


  //  printGraph(graph);

   fclose(input_file);
  return 0;
}
