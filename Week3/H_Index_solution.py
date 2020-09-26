n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort(reverse = True)
h_index = 0
for i, num_paper in enumerate(arr):
    if num_paper >= i+1:
        h_index = i+1
    else:
        break
print(h_index)