#include <bits/stdc++.h>
using namespace std;

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int knapSack(int W, int wt[], int val[], int n)
{
    int i, w;
    int K[n + 1][W + 1];

    for(i = 0; i <= n; i++)
    {
        for(w = 0; w <= W; w++)
        {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] +
                                K[i - 1][w - wt[i - 1]],
                                K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }

    for(i = 0; i <= n; i++)
    {
        for(w = 0; w <= W; w++)
        {
            cout<<K[i][w]<<"  ";
        }
        cout<<endl;
    }
    return K[n][W];
}

int main() {

    int m = 6;

    ifstream infile;
    infile.open("C:/Users/1625203/Desktop/lol.txt");
  int profits[m];
  int weights[m];
  int idx = 0;
	int v1, v2;
    while (infile >> v1 >> v2)
 	{
  		profits[idx] = v1;
  		weights[idx] = v2;
  		idx++;
 	}

 	float alltime=0;

 	int n = sizeof(profits) / sizeof(profits[0]);
    cout << knapSack(7, weights, profits, n);

}
