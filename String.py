# Bài 1 :
# Mục đích chính của dấu 3 nhấy là dùng để comment
'''Escape Sequence
\a : Phát ra 1 tiếng bíp
\b : Đưa con trỏ về 1 khoảng trắng
\n : Đưa con trỏ về dòng tiếp theo
\t : In 1 horizontal tab
\' : In ra ký tự '
\" : In ra ký tự "
\\ : In ra ký tự \
'''
#print("\a")

# Mất chữ e tại vì sau nó là \b
#print("abcde\bf") 
# Căn dòng
#print("Hello\nAre U Good")

# Bài 2 :
# Chuổi trần dùng để tránh việc gặp lỗi Escape Sequence(\) khi bỏ đường dẫn.Ví Dụ:
#print(r"ổ C\thư mục a\thu mục d")

# Hàm "In" kiểm tra xem biến 1 có nằm trong biến khác hay ko . Ví dụ:
#strA = "Abcdef"
#strB = "a"
##strC = strB in strA
# Kiểm tra xem B có nằm trong A hay ko 
#print(strC)

# Hàm "len" lấy độ dài của chuổi
#print(len(strA))

# 1 Trong những khả năng đặc biệt khác của Python là cắt chuổi. Ví dụ:
# lấy từ index từ 1 tới cuối chuổi
#print(strA[1:len(strA)])
# Hoặc 1 cách khác gọn hơn là dùng tới "None"
#print(strA[1:None])


# Ép kiểu . Ví dụ :
# a =int("6") + 5
# ép chuổi String = 6 sang kiểu int và cộng với 5   
# print(a)


# Định dạng chuỗi trong Python
noiChuoi = "My name is %s , How are u today" %("Tuan")
noiChuoi2 = "My name is %s , How %s u today" %("Liam","are")
print(noiChuoi)
print(noiChuoi2)

""" Một số các toán tử % cơ bản trong Python
%s : Giá trị của phương thức __str__của đối tượng đó
%r : Giá trị của phương thức __repr__ của đối tượng đó
%d : Giá trị của 1 số chỉ lấy phần nguyên
%<Số phần thập phân>f : Giá trị của 1 số - Nếu là số sẽ được chuyển sang số thực.
"""


# Định dạng = chuổi f(f-string) . Ví dụ :
var = 'Team A'
result = f'{var} - Ở Đây !'
# var ở trong result là biến var đã tạo sẵn ở trên
print(result)

# Định dạng = phương thức format (Nên dùng) . Ví dụ :
r = '1: {1}, 2: {0}, 3: {2}'.format(3,2,1)
print(r)
# Định dạng format còn giúp căn lề 1 cách thẩm mỹ.
canGiua = 'Đây là {:^10} nè'.format('kteam') 
canTrai = '{:<10} Alo'.format('kteam')
canPhai = 'Alo {:>10}'.format('kteam')

print(canGiua)
print(canTrai)
print(canPhai)

# Ví dụ có thể tạo ra nội dung với File Python như sau :
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'ABC', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'CDE', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)