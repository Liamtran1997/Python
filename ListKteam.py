# Kiểu dữ liệu "List"
"""
1. Giới hạn bởi cặp ngoặc vuông
2. Các phần tử của List cách nhau bởi dấu phẩy
3. List có khả năng chứa mọi giá trị đối tượng của Python
4. Và bao gồm chính nó 
"""
# Khởi tạo 1 List
# myList = [1,2,"ABC",True]
# print(myList)

# List Comprehension (Vòng lặp trong list)
# listComprehension = [i for i in range(0,4)]
# listComprehension2 = [[i,i*2,i*3] for i in range(0,4)]
# Tạo ra 1 List và gán vào biến listComprehension. Với List được tạo ra chạy từ 0 đến 4 đơn vị
# print(listComprehension)
# print(listComprehension2)

# List Iterable
# strList = list("HowKteam")
# print(strList)

# strList2 = [1,2,3,4,5]
# strList3 = strList2
# print(strList2)
# print(strList3)
# strList3[0] = "Kteam"
# print(strList2)
# print(strList3)
# Khi gán 1 List cho 1 list khác nên để không bị trùng lặp vùng nhớ 
# Làm như trên khiến strList3 thay đổi kéo theo strList2 cũng thay đổi . Nên để như sau
# strList3 = list(strList2)



# Các Phương thức tiện ích.
# Count . Đếm xem số lần xuất hiện của 1 phần tử trong List là bao nhiêu lần
sampleList = [1,2,3,2,4,5,6]
a = sampleList.count(2)
print(a)
# Index . Trả ra vị trí của phần tử đó nằm trong List, Nếu có nhiều thì lấy cái đầu tiên
# Copy . Tạo ra 1 bảng sao của List đã copy mà không trở tới cùng 1 giá trị 
# Clear . Xóa mọi phần tử trong List



# Các Phương thức cập nhật.
# Phương thức append . Thêm phần tử mới vào cuối List đã tạo ra trước đó
sampleList.append(7)
print(sampleList)

# Phương thức Extend gần như tương tự Append
# Phương thức Insert . Là thêm phần tử x vào vị trí i. <List>.insert (i, x)
sampleList.insert(3,4)
print(sampleList)
# Phương thức Pop tương tự Insert nhưng lại là bỏ đi thay vì thêm vào



# Các Phương thức xử lý.
# Phương thức reverse. Đảo ngược list đang có
# Phương thức sort. Sắp xếp list đang có 
sampleList.sort()
print(sampleList)