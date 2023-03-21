#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <list>
#include<unordered_map>
#include <fstream>
#include <time.h>
using namespace std;

    vector < list<int> > graph;
    vector <int> deg;
    stack<int> head,tail ;

int main()
{
    int n=700, x,y;
    ifstream infile;
    infile.open("C:/Users/1625203/Desktop/A&DS I/A&DS Report 4/Eu-700-0.9.txt");

    graph.resize(n+1);
    deg.resize(n+1);
    while (infile >> x >> y)
    {
        graph[x].push_back(y);
        graph[y].push_back(x);
        ++deg[x];
        ++deg[y];
    }
    float time = 0;
    for(int i = 0; i < 10; i++){
    const clock_t begin_time2 = clock();
    if(any_of(deg.begin()+1,deg.end(),[](int i){return i&1;}))
        cout << "-1";
    else
    {
        head.push(1);
        while(!head.empty())
        {
            while(deg[head.top()])
            {
                int v = graph[head.top()].back();
                graph[head.top()].pop_back();
                graph[v].remove(head.top());
                --deg[head.top()] ;
                head.push(v);
                --deg[v];
            }
            while(!head.empty()&&!deg[head.top()])
            {
                tail.push( head.top());
                head.pop();
            }
        }

        while(!tail.empty())
        {

            tail.top();
            tail.pop();
        }

    }
    time += float( clock () - begin_time2 ) /  CLOCKS_PER_SEC;
    }
    cout << float(time/10);
}
