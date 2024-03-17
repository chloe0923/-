#include<iostream>
using namespace std ;

constexpr int DIMENSION_SIZE = 35 ;
constexpr int QUEUE_MAX_SIZE = DIMENSION_SIZE*DIMENSION_SIZE*DIMENSION_SIZE+5 ;
struct Point{
  int l, r, c ;
};

int L, R, C, steps[DIMENSION_SIZE][DIMENSION_SIZE][DIMENSION_SIZE] ;
char maze[DIMENSION_SIZE][DIMENSION_SIZE][DIMENSION_SIZE] ;
bool visited[DIMENSION_SIZE][DIMENSION_SIZE][DIMENSION_SIZE] ;
Point queue_node[QUEUE_MAX_SIZE] ;
Point start_p, end_p ;
int q_len, q_current ;
// 0:up(l+1), 1:down(l-1), 2:front(r+1), 3:back(r-1), 4:right(c+1), 5:left(c-1), -1:none
int from[DIMENSION_SIZE][DIMENSION_SIZE][DIMENSION_SIZE] ;

void tryPushQueue(int l, int r, int c, int s, int f){
  if(l>=L || r>=R || c>=C || l<0 || r<0 || c<0 ||
     visited[l][r][c] || maze[l][r][c]=='#') return ;
  visited[l][r][c] = true ;
  steps[l][r][c] = s ;
  from[l][r][c] = f ;
  queue_node[q_len] = {l, r, c} ;
  q_len++ ;
}

int main(){

  while(cin>>L>>R>>C){
    if(L==0 && R==0 && C==0) break ;
    for(int l=0 ; l<L ; l++){
      for(int r=0 ; r<R ; r++){
        for(int c=0 ; c<C ; c++){
          cin>>maze[l][r][c] ;
          if(maze[l][r][c]=='E') start_p={l, r, c} ;
          else if(maze[l][r][c]=='S') end_p={l, r, c} ;
          visited[l][r][c] = false ;
          steps[l][r][c] = -1 ;
          from[l][r][c] = -1 ;
        }
      }
    }
    q_len = 0 ;
    tryPushQueue(start_p.l, start_p.r, start_p.c, 0, -1) ;
    q_current = 0 ;
    while(q_current<q_len){
      const int l=queue_node[q_current].l ;
      const int r=queue_node[q_current].r ;
      const int c=queue_node[q_current].c ;
      const int s=steps[l][r][c] ;
      tryPushQueue(l+1, r, c, s+1, 1) ;
      tryPushQueue(l-1, r, c, s+1, 0) ;
      tryPushQueue(l, r+1, c, s+1, 3) ;
      tryPushQueue(l, r-1, c, s+1, 2) ;
      tryPushQueue(l, r, c+1, s+1, 5) ;
      tryPushQueue(l, r, c-1, s+1, 4) ;
      q_current++ ;
    }

    if(!visited[end_p.l][end_p.r][end_p.c]) cout << "Trapped!" << endl ;
    else{
      int l=end_p.l, r=end_p.r, c=end_p.c ;
      cout << "Escaped in " << steps[l][r][c] << " minute(s)." << endl ;
      while(true){
        cout << "(" << l << ", " << r << ", " << c << ")" << endl ;
        if(from[l][r][c]==0) l++ ;
        else if(from[l][r][c]==1) l-- ;
        else if(from[l][r][c]==2) r++ ;
        else if(from[l][r][c]==3) r-- ;
        else if(from[l][r][c]==4) c++ ;
        else if(from[l][r][c]==5) c-- ;
        else break ;
        if(maze[l][r][c]!='E') maze[l][r][c] = '*' ;
      }
      for(int l=0 ; l<L ; l++){
        for(int r=0 ; r<R ; r++){
          for(int c=0 ; c<C ; c++) cout << maze[l][r][c] ;
          cout << endl ;
        }
        cout << endl ;
      }
    }
  }
  return 0 ;
}
