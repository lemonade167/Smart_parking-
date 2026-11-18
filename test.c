#include "parksmart.h"
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
int main(void){System *s=malloc(sizeof(System));assert(s);init_system(s);s->nodes=2;s->count=1;s->spaces[0]=(Space){.id=1,.node=1,.capacity=1,.rate=20,.active=1};s->graph[0][1]=s->graph[1][0]=7;assert(nearest_space(s,0,10,12,0)==0);int id=reserve_space(s,1,"Test",10,12);assert(id>0);assert(reserve_space(s,1,"Other",11,13)==-2);assert(reserve_space(s,1,"Other",12,14)>0);assert(cancel_reservation(s,id));assert(available(s,0,10,12));int a[]={5,1,3,2,4};merge_sort(a,5);assert(binary_search_iter(a,5,3)==2);assert(kmp_search("parking reservation","reservation")==8);assert(knapsack((int[]){2,3,4},(int[]){3,4,5},3,5)==7);assert(nqueens_count(4)==2);assert(crt_pair(2,3,3,5)==8);puts("All C smoke tests passed.");free(s);return 0;}
