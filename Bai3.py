# Cho 1 dãy số , tính tổng dãy đó với for loop

set = {2,4,5,2,6,7,1}
sum_all = 0

for value in set:
    sum_all += value

print("Tổng = "+str(sum_all))



# Tổng trung bình cộng các số nhập vào từ bàn phím
num = int(input("Nhập số lượng phần tử trong mảng : "))
a = []
for i in range(0,num):
    elme = int(input("Nhập số mong muốn :  "))
    a.append(elme)
    
avg = sum(a) / num
print("Giá trị trung bình của mảng : "+ str(avg))
