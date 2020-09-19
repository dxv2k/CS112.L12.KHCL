# Longest increasing sequence
from math import *
def solution(n,alpha,list_coord): 
    cnt_stars = 0 
    tan_alpha = tan(alpha)
    return cnt_stars 





n = int(input())
a,b,c,d = map(int,input().replace(' ','/').split('/')) 

alpha = atan2(c,d) - atan2(a,b) 

list_coord = [] # contains star coordinates 

for i in range(n): 
    x,y = map(int,input().split())
    list_coord.append([x,y])

solution(n,alpha,list_coord) 





