n = int(input())
a = list(map(int, input().split()))
p = 0
q = 0
temp_p = 0
temp_profit = a[0]
profit = -99999

for i in range(1, n):
    temp_profit = temp_profit + a[i]
    if temp_profit > profit:
        profit = temp_profit
        q = i
        p = temp_p
    if temp_profit < 0:
        temp_profit = 0
        temp_p = i + 1
print(p + 1, q + 1, profit)