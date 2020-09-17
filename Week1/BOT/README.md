## 1. Abstract
- Given N tracks.
- Found continous `p`, `q` parts that bring the most return on investment.
## 2.Pattern Recoginition
- Maximum continous subarray.
## 3.Algorithm designed
- Dynamic programming.
- Input:
  - `n`: Number of track.
  - `arr`: Array for save infomation of the part of track.
- Output: `p`: position where the track start.
  - `q`: position where the track end.
  - `profit`: the best profit of the path.
- Temporary variable: `temp_p`, `temp_profit`. We need a tempary variables for p and profit cause the profit and the start position p can be changed if the condition is not.
- Condition: 
  - If the `temp_profit` > `profit` (mean the value of the `temp_profit` at the moment is maximum) then assign this value to `profit` and update value `p`
  - If the `temp_profit` < 0 (means the value of `temp_profit` is negative and we don't want to invest our money on that road) then reset the value of `temp_profit` and update the value of the the `temp_p` to the next position.

Description (Psudo code):
```python
temp_p = 0
temp_profit = 0
p = 0
q = 0
profit = -inf 
for i := 1 -> n 
    temp_profit =  temp_profit + a(i)
    if temp_profit > profit then
        profit <- temp_profit
        q <- i
        p <- temp_p
    if temp_profit < 0 then
        reset temp_profit (temp_profit = 0)
        temp_profit <- i + 1
```
- Time complexity: O(n)
4. [Source code](./solution.py)
5. [Jupiter notebook version](./solution.ipynb)