## 1. Abstract
- Given N tracks  
- Found continous p,q parts that bring the most return on investment
## 2.Pattern Recoginition
- Maximum continous subarray
## 3.Algorithm designed
- Dynamic programming
- Input: `n`: , `arr`: 
- Output: `start_track_pos`, `end_track_pos`, `return_on_investment_result`
- Temporary: 
- Condition: 
    
- Description:
```python
if current sum < arr[i]:
    ignore current sum
    sum = arr[i]
sum, result = 0,0
for i = 0 -> n: 
    sum = max(arr[i], sum + arr[i])
    result = max(result,sum) 
return result
```
- Time complexity: O(n) # Not sure about this
