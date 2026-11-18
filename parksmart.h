#ifndef PARKSMART_H
#define PARKSMART_H
#define MAX_SPACES 300
#define MAX_RESERVATIONS 2000
#define MAX_NODES 100
#define INF 100000000

typedef struct {int id,node,capacity,occupied,rate,active; char name[64];} Space;
typedef struct {int id,space_id,start,end;char driver[64];int active;} Reservation;
typedef struct {Space spaces[MAX_SPACES];int count;Reservation reservations[MAX_RESERVATIONS];int rcount;int graph[MAX_NODES][MAX_NODES];int nodes;int next_id;} System;
void init_system(System *s);
int load_system(System *s,const char *dir);
int save_system(const System *s,const char *dir);
int reserve_space(System *s,int id,const char *driver,int start,int end);
int cancel_reservation(System *s,int id);
int available(const System *s,int idx,int start,int end);
int shortest_paths(const System *s,int source,int dist[MAX_NODES]);
int nearest_space(const System *s,int source,int start,int end,int *distance);
int greedy_assign(const System *s,const int *drivers,int nd,int start,int end,int *assignment,int *total);
int optimal_assign(const System *s,const int *drivers,int nd,int start,int end,int *assignment,int *total);
void merge_sort(int *a,int n);
void quick_sort(int *a,int n);
int binary_search_iter(const int *a,int n,int key);
int binary_search_rec(const int *a,int l,int r,int key);
int kmp_search(const char *text,const char *pattern);
int rabin_karp_search(const char *text,const char *pattern);
int naive_search(const char *text,const char *pattern);
int max_subarray(const int *a,int n);
long long fast_power(long long a,unsigned int b);
int knapsack(const int *w,const int *v,int n,int capacity);
int lcs_length(const char *a,const char *b);
int nqueens_count(int n);
int subset_sum(const int *a,int n,int target);
int crt_pair(int a,int m,int b,int n);
int prim_mst(const System *s);
int kruskal_mst(const System *s);
int bellman_ford(const System *s,int source,int *dist);
void floyd_warshall(const System *s,int dist[MAX_NODES][MAX_NODES]);
int tsp_exact(const System *s,int *nodes,int n);
int max_bipartite_matching(int rows,int cols,const int edges[32][32]);
int ford_fulkerson(int n,int cap[32][32],int source,int sink);
#endif
