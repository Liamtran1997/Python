# 1.
# Capitalize dùng để viết hoa chữ đầu tiên.
word = "howKteam"
word2= word.capitalize()

print(word)
print(word2)

# Phương thức Upper và Lower.
# Upper giúp in hoa tất cả và Lower ngược lại
upperWord = "howkteam".upper()
lowerWord = "HOWKTEAM".lower()

print(upperWord)
print(lowerWord)

# Phương thức SwapCase và Title.Cho phép đỗi chỗ và In hoa những chữ cái đầu tiên
swapCaseWord = "howkteam  THERE".swapcase()
titleWord = "HOWKTEAM HELLO".title()
print(swapCaseWord)
print(titleWord)


# 2.Các phương thức định dạng
# Center dùng để căng giữa.Ví dụ :
centerWord = "Kteam".center(20,"$")
print(centerWord)

# Căn phải sẽ là rjust và trái sẽ là ljsut
rightWord = "Kteam".rjust(20)
leftWord = "Kteam".ljust(20)

print(rightWord)
print(leftWord)

# 3.Các phương thức xử lý.
# Phương thức encode. Dùng để mã hóa thông tin. Ví dụ :
encodeString = "Có ai ở đây không".encode()
print(encodeString)

# Phương thức Join
joinString = "Có ai ở đây không".join(["a","b","c"])
print(joinString)
# Có nghĩa là  a+joinString+b+joinString+c

# Phương thức replace. Dùng để thay thế các ký tự hay các chuỗi lại với nhau. Ví dụ :
replaceString = "Có ai ở đây không"
replaceString2 = "Có ai ở đây không".replace("ai","người nào")

print(replaceString)
print(replaceString2)

