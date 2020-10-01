Click the badge bellow to use Google Colab for better render result!!!

<a href="https://colab.research.google.com/github/dxv2k/CS112.L12.KHCL/blob/Week-3/Week3/H_Index_solution.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# H Index problem
Ví dụ ta cho 5 số nguyên 
` 8 , 5 , 3 , 4 , 10 `

Nếu:
- `k = 1`, có 5 số $\geq 1$ ($5 \geq 1$)
- `k = 2`, có 5 số $\geq 2$ ($5 \geq 2$)
- `k = 3`, có 5 số $\geq 3$ ($5 \geq 3$)
- `k = 4`, có 4 số $\geq 4$ ($4 \geq 4$)
- `k = 5`, có 3 số $\geq 5$ ($3 \leq 5$) -> Loại

Kết luận: `H_Index = 4`

## 1. Abstraction
Tìm `H_Index` sao cho `H_Index` là số `k` lớn nhất thoả điều kiện các phần tử trong dãy lớn hơn hoặc bằng `k`

## 2. Pattern Recognition
Gọi dãy `arr` là dãy bao gồm các phần tử chỉ số lượng trích dẫn bài báo. Sắp xếp dãy `arr` theo thứ tự giảm dần. Thực hiện duyệt phần tử. Tại mỗi vị trí thứ `i` ta so sánh giá trị `arr[i]` có $\geq$ `i` không? Nếu có thì `H_Index` tăng một giá trị.

## 3. Design Algorithm
Pseudocode
```python
H_Index = 0
for i in range(arr): # Duyệt tất cả các phần tử trong mảng
    if arr[i] >= i:
        H_Index += 1 # Tăng một giá trị
    else:
        break # Nếu mà bé hơn thì dừng vòng lặp
return H_Index
```