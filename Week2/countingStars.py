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
    x, y = map(int,input().split())
    transform(x, y)
    list_coord.append([x,y])

def transform(x, y):
    if (y > (a/b)*x) and (y < (c/d)*x):
        r = sqrt(x**2 + y**2)
        temp = atan(y/x) - atan(a/b)
        x = r * cos(temp)
        y = r * sin(temp)

def sort_y(list_coord):
    list_coord.sort(key = lambda x: x[1] - tan(alpha)*x[0], reversed = True)

def 
solution(n,alpha,list_coord)
# Eliminate point out of range

