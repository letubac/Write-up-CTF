+ Ở bài này mình được cung cấp 1 fie Encrypt.exe và file Flag.txt.enc

![image](https://user-images.githubusercontent.com/57956165/140247741-934a6431-078b-406e-965e-7308405c1ffd.png)

+ Mình sử dụng ida pro 64 để load file vào, bấm f5 để vào chương trình chính, đoạn code ở trên mình bỏ qua, ở đây mình thấy hàm Encrypt, nhấp chuột vào xem cụ thể hơn hàm đó làm gì

![image](https://user-images.githubusercontent.com/57956165/140246462-e8ae9d25-e55c-446c-a92b-dcf782550f5b.png)

+ Nhìn vào đống code này có vẻ khá hiểu, bây giờ mình sẽ phân tích cho mọi người dễ hiểu hơn

![image](https://user-images.githubusercontent.com/57956165/140246711-4c46ef92-65fa-4aa2-8d16-68dd5866f0de.png)

+ Đầu tiên ở hàm if này nó sẽ kiểm tra tất cả các file này có toofn tại hay không

![image](https://user-images.githubusercontent.com/57956165/140246820-b027ac3a-ff7d-4541-8476-0d29558d9e2b.png)

+ Hàm if tiếp theo nó sẽ kiểm tra xem có file .enc nào không, nếu tồn tại thì nó sẽ xuất thông báo "Encrypt file 100%"

![image](https://user-images.githubusercontent.com/57956165/140247059-0d18a6ca-6527-43fc-ba5c-958774bcbbb4.png)

+ Tiếp theo bạn chú ý tới dòng này, dòng này sẽ là dữ liệu để chút nữa chúng ta sử dụng đi decrypt nó 
# V27 = 412

![image](https://user-images.githubusercontent.com/57956165/140247476-595a8030-7776-4a6d-b87a-57570f755459.png)

+ Ở đoạn code tiếp theo nó sẽ sử dụng ifstream và ofstream để đọc và ghi file

![image](https://user-images.githubusercontent.com/57956165/140247831-4dee103b-ddd3-475f-ba9b-0269127df41d.png)

+ Ở đoạn code này, nó sẽ đọc tất cả các ký tự ở trong file, mỗi lần đọc một ký tự thì nó sẽ cộng với V27

![image](https://user-images.githubusercontent.com/57956165/140248225-f5c0c661-95c9-4118-b37f-c40094eece78.png)

+ Bây giờ để decrypt thì mình chỉ cần lấy từng ký tự trong file .enc - V27 là xong

- Đây là mã C của tôi, sau khi chạy chương trình thì tôi nhận được flag:

![image](https://user-images.githubusercontent.com/57956165/140248383-c92ec733-03b3-4ab4-a83f-1743f29c855b.png)

# Flag: WhiteHat{D3crypt_me_ahihi}
