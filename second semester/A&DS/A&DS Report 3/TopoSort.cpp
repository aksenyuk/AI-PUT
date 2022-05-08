#include<iostream>
#include <list>
#include <stack>
#include <fstream>
#include <time.h>
#include <chrono>

const int n = 6000;

using namespace std;

class G {
   int n;
   list<int> *adj;

   void topologicalSort(int v, bool visited[], stack<int> &Stack);
   public:
   G(int n);
   void addEd(int v, int w);
   void topoSort();
};
G::G(int n) {
   this->n = n;
   adj = new list<int> [n];
}
void G::addEd(int v, int w)  {
   adj[v].push_back(w);
}

void G::topologicalSort(int v, bool visited[], stack<int> &Stack) {
   visited[v] = true;
   list<int>::iterator i;

   for (i = adj[v].begin(); i != adj[v].end(); ++i)
      if (!visited[*i])
         topologicalSort(*i, visited, Stack);
         Stack.push(v);
}

void G::topoSort() {
   stack<int> Stack;
   bool *visited = new bool[n];

   for (int i = 0; i < n; i++)
      visited[i] = false;
      for (int i = 0; i < n; i++)
         if (visited[i] == false)
            topologicalSort(i, visited, Stack);
         while (Stack.empty() == false) {
            //cout << Stack.top() << " "; //print the element
            Stack.top();
            Stack.pop();
         }
}


int main() {
    ifstream infile;
    infile.open("C:/Users/1625203/Desktop/input edges.txt");
   G g(n);

   	int v1,v2;

    while (infile >> v1 >> v2)
 	{
  		g.addEd(v1, v2);
 	}

   cout << " Topological Sort of the given graph \n";

    double alltime=0;

    for (int i = 0; i < 10; i++){
        //const clock_t begin_time2 = clock();
        auto start = std::chrono::high_resolution_clock::now();
        g.topoSort();
        auto elapsed = std::chrono::high_resolution_clock::now() - start;
        //cout<<float( clock () - begin_time2 ) /  CLOCKS_PER_SEC<<endl ;
        double microseconds = std::chrono::duration_cast<std::chrono::microseconds>(elapsed).count();
        microseconds = double(microseconds / 1000000);
        cout<<microseconds<<endl;
        alltime += microseconds;
    }

    cout<<endl<<endl<<alltime/10<<endl<<endl;

   return 0;
}
