from functools import reduce

# Một số hàm bổ trợ  : 
# Filter
# Lấy ra số lớn hơn 0 
func = lambda x: x > 0
lst = [1, -3, 5, 0, 2, 6, -4, 9]
print(list(filter(func,lst))) 


# Reduce 
# Tính tổng hàm chuyền vào
add = lambda a, b: a + b
lst_2 = [1,4,5,6,7,9]
total = reduce(add,lst_2)

print("Tổng giá trị của lst_2 = " + str(total))

