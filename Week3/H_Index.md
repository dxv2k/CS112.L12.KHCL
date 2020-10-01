# H_Index (1s, 100MB)
Làm thế nào để đánh giá sự thành công của một nhà khoa học?  Dựa vào số bài báo được công bố hay dựa vào số lần một bài báo được trích dẫn tới ở công trình của những người khác? Cả hai tham số đó đều quan trọng.

Một bài báo có điểm số trích dẫn là `c` nếu nó được trích dẫn tới `c` lần trong các công trình của những nhà khoa học khác. Một trong số các cách đánh giá sự thành công của một nhà khoa học là tính chỉ số ảnh hưởng `H_Index` dựa trên sự kết hợp giữa số lượng bài báo và chỉ số trích dẫn của các bài báo đó.

Chỉ số `H_Index` của một nhà khoa học bằng `k` lớn nhất nếu người đó có `k` bài báo, mỗi bài có điểm số trích dẫn không nhỏ hơn `k`. Ví dụ, một người có 10 bài báo, mỗi bài báo được trích dẫn không dưới 10 lần thì `H_Index` của người đó ít nhất là bằng 10.

Một người có `n` bài báo, bài báo thứ `i` có điểm trích dẫn là ![formula](https://render.githubusercontent.com/render/math?math=c_{i},i%20=1\div%20n). Hãy xác định `H_Index` của người đó.

Dữ liệu: Vào từ thiết bị nhập chuẩn:
- Dòng đầu tiên chứa một số nguyên ![formula](https://render.githubusercontent.com/render/math?math=n%20(1%20\leq%20n\leq%205\times10^5)),
- Dòng thứ 2 chứa n số nguyên ![formula](https://render.githubusercontent.com/render/math?math=c_1,c_2,...,c_n(0\leq%20c_i\leq10^6,i=1\div%20n)).

Kết quả: Đưa ra thiết bị xuất chuẩn một số nguyên – `H_Index` tìm được.

Ví dụ:
| INPUT              | OUTPUT |
|--------------------|--------|
| 5 <br> 8 5 3 4 10  | 4      |