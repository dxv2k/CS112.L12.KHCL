# input n BOT
n = int(input())
# input the profit of every single BOT
a = list(map(int, input().split()))
# assign value for p and q = 0
p = 0
q = 0
# create a temp variable for p
temp_p = 0
# create a temp variable for the total profit
temp_profit = a[0]
# assign minus infinite value for the total profit
profit = -99999

for i in range(1, n):
    # calculate the profit and assign the value to temp_profit variable
    temp_profit = temp_profit + a[i]
    # if the value is larger than the profit then assign that value to the profit, increase q and assign value of temp_p to p
    if temp_profit > profit:
        profit = temp_profit
        q = i
        p = temp_p
    #if temp_profit < 0 (means that sub_array has the negative total_profit) then we skip that subarray by increase the p and assign 0 value to temp_profit
    if temp_profit < 0:
        temp_profit = 0
        temp_p = i + 1
print(p + 1, q + 1, profit)