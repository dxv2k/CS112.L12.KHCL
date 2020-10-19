def solution(a,b): 
    dict = {}
    cnt = 0

    for i in range(0,len(a)-1):
        if (a[i] + a[i+1]) not in dict:
            dict[ a[i] + a[i+1] ] = 1
        else:
            dict[ a[i] + a[i+1] ] += 1

    for i in range(0,len(b)-1):
        if (b[i] + b[i+1]) in dict:
            cnt += 1
    return cnt

a = input().strip()
b = input().strip()

print(solution(b,a))
