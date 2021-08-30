# Dùng đến Lambda

# So sanh 2 số với Lambda :
find_num = lambda a,b : a if a > b else b
print(find_num(1,3))


# Kiểm tra số chẵn số lẽ với lambda
check_num = lambda num: print("Số nhập vào là số chẵn") if num % 2 == 0 else print("Số nhập vào là số lẽ")

print(check_num(11))