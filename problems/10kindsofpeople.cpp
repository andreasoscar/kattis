#include <iostream>
#include <bits/stdc++.h>
#include <list>
#include <string>
using namespace std;

class Graph{
  private:
    int V;
    list<int> *adj;
  public:
    Graph(int v);
    void addEdge(int v, int w);
    void BFS(int s);
};

Graph::Graph(int v){
  V = v;

  adj = new list<int>[v];
}

void Graph::addEdge(int v, int w){
  adj[v].push_back(w);
}

void Graph::BFS(int s){
  bool *visited = new bool[V];
  for(int i=0; i < V; i++){
    visited[i] = false;
  }
  list<int> queue;
  visited[s] = true;
  queue.push_back(s);

  while(!queue.empty()){
    s = queue.front();
    queue.pop_front();

    for(auto i = adj[s].begin(); i != adj[s].end(); i++){
      if(!visited[*i]){
        visited[*i] = true;
        cout << "visited: " << *i << endl;
        queue.push_back(*i);
      }
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int x,y;
  cin >> y >> x;
  int matrix[x][y];
  for(int i = 0; i < y; i++){
    string t;
    cin >> t;
    for(int j=0; j < x; j++){
      int c = t[j] - '0';
      cout << "(" + to_string(i+1) + "," + to_string(j+1) + ") = " + to_string(c) << endl;
      matrix[j][i] = c;
      cout << matrix[i][j] << endl;
    }
  }
  Graph g(max(x,y));
}
