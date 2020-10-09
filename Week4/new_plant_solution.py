a,k,b,m,n = map(int,input().split()) 

def f(x): 
    return a*(x-x//k) + b*(x-x//m) >= n 

res = -1 
low = 0 
high = int(1e18)

while low <= high: 
    mid = (low+high)//2 
    if f(mid): 
        res = mid 
        high = mid - 1
    else: 
        low = mid + 1
print(res)





