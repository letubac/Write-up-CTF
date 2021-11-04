
+ Kiểm tra thấy nó là file ELF-64 bit, tôi sử dụng ida pro 64 load file lên

![image](https://user-images.githubusercontent.com/57956165/140244159-646b1095-c709-4899-8510-d9eea7a4e358.png)

+ F5 đề vào xem chương trình chính code c
+ Ở đây, chương trình sẽ lấy chuỗi "WikwaMgss[9}?_}>~VMZgJ%Wk`g" đi xử lý

+ Sau đó nó sẽ lấy từng ký tự của chuỗi đó XOR với chiều dài của nó
+ Nếu chuỗi đó bằng với chuỗi input thì xuất ra thông báo "Congratulate", ngược lại thì "Wrong"

![image](https://user-images.githubusercontent.com/57956165/140245123-91c9e604-9772-476a-bdfd-b49b9c60dcdb.png)

+ Sau đó tôi sẽ viết lại code python để thực hiện đoạn XOR của mã nguồn c

![image](https://user-images.githubusercontent.com/57956165/140245208-0f9b9ac5-c9f7-488d-b751-376c0b956006.png)

# Flag: WhiteHat{R3v3Rs1nG_Is_3@sy}
