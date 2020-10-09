# Tái cấu trúc
Sau thời gian làm việc tại nhà (work from home) do tình hình dịch bệnh, công ty X nhận thấy đây là cơ hội để thay đổi mô hình làm việc của công ty để hướng tới tính đơn giản, hiệu quả cao hơn trong công việc. Cụ thể, công ty hiện tại gồm `n` nhân viên. Có `m` quan hệ dạng (ai, bi) trong đó người bi nhận công việc từ người ai và ai chỉ đạo cho bi. Mỗi nhân viên khi nhận việc có thể phân công cho những nhân viên do mình chỉ đạo. Nếu công viêc từ `a` có thể tới được `b`, ta gọi `a` là cấp trên của `b` và `b` là cấp dưới của `a`.

Sau khi họp đại hội cổ ccông trực tuyến, công ty X quyết định thực hiện tái cấu trúc như sau:
- Thứ nhất, chọn ra một giám đốc, người này phải là người không có cấp trên và công việc mà người này phân công có thể tới được mọi người trong công ty
- Những người còn lại, mỗi người sẽ chỉ còn nhận việc trực tiếp từ đúng 1 người. Để tránh xáo trộn trong hoạt động sau khi thực hiện thay đổi, với mỗi người, tập những người là cấp trên của người đó phải không thay đổi (so với trước khi thực hiện tái cấu trúc).

Yêu cầu: Xác định công ty X có thể tái cấu trúc hay không, nếu không được - đưa ra thông báo “No”. Trong trường hợp có thể – đưa ra thông báo “Yes” và chỉ ra dãy số pi xác định người có quyền phân công công việc cho người i (1 ≤ i ≤ n). Với Giám đốc pi tương ứng có giá trị là -1.

**Dữ liệu**: Vào từ file thiết bị nhập chuẩn:

Dòng đầu tiên chứa 2 số nguyên n và m (1 ≤ n, m ≤ 5×10^5),
Dòng thứ i trong m dòng sau chứa 2 số nguyên ai và bi (1 ≤ ai, bi ≤ n, ai ≠ bi).

**Kết quả**: Đưa ra thiết bị xuất chuẩn thông báo “No” hoặc “Yes”. Nếu kết quả là “Yes” – trên dòng thứ 2 đưa ra n số nguyên p1, p2, . . ., pn tương ứng.

**Ví dụ**:
| INPUT                           | OUTPUT        |
|---------------------------------|---------------|
| 3 3<br>1 2<br>2 3<br>1 3        | Yes<br>-1 1 2 |
| 4 4<br>1 2<br>1 3<br>2 4<br>3 4 | No            |