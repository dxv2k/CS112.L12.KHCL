# KHÔI PHỤC HỆ THỐNG CẤP NƯỚC (1s, 100MB)

Vùng đất diệu kỳ Wonderland có `N` hộ gia đình đã được trang bị một hệ thống cung cấp nước sạch đến từng ngôi nhà. Mỗi đường ống nối trực tiếp 2 nhà, nước chảy trong đường ống theo 2 chiều, có thể truyền qua nhiều trung gian trước khi đến một nhà nào đó. Trong hồ sơ lưu trữ, các ngôi nhà được ghi số từ 1 đến `N`.

Một trận động đất đã gây nên sự cố nghiêm trọng làm cho cả vùng bị chia cắt thành nhiều khu vực rời nhau, không còn tiếp cận được với nguồn nước. Để khắc phục, những người có trách nhiệm đã khảo sát hiện trạng và ghi nhận được toàn vùng đất đang thảm họa vẫn còn `M` đường ống đang hoạt động tốt.

Nhiệm vụ đặt ra là phải khôi phục hệ thống cấp nước bằng cách lắp thêm một số đường ống. Tuy nhiên, do hạn chế về thời gian và kinh phí nên đòi hỏi phương án khôi phục phải được thực hiện với ít đường ống được lắp thêm nhất. Câu hỏi đặt ra: cần lắp thêm ít nhất bao nhiêu đường ống để hệ thống cấp nước có thể đưa nước đến từng ngôi nhà. Câu hỏi phụ: có bao nhiêu phương án khác nhau đáp ứng yêu cầu; số phương án có thể khá lớn nên chỉ cần đưa ra số dư khi chia cho 109+7.

Dữ liệu: Vào từ thiết bị nhập chuẩn:

- Dòng đầu tiên chứa 2 số nguyên `N`, `M` ![formula](https://render.githubusercontent.com/render/math?math=(1%20\leq%20N,M%20\leq10^5))
- Mỗi dòng trong M dòng tiếp theo chứa 2 số nguyên `a`, `b` ![formula](https://render.githubusercontent.com/render/math?math=1%20\leq%20a,%20%20b%20\leq%20N). Cho biết vẫn còn đường ống nối nhà `a` với nhà `b`

Kết quả: Đưa ra thiết bị xuất chuẩn số đường ống cần được lắp thêm và số phương án đáp ứng yêu cầu (theo mô đun ![formula](https://render.githubusercontent.com/render/math?math=10^9+7)) mỗi số trên một dòng.

Dữ liệu mẫu:

| INPUT | OUTPUT |
|-------|--------|
| 3 1   | 1      |
| 1 2   | 2      |