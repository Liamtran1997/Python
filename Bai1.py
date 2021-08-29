# Nhập 2 số nguyên từ bàn phím và tính tổng

print("Nhập số thứ nhất vào bàn phím")
int_1 = int(input())
print("Nhập số thứ hai vào bàn phím")
int_2 = int(input())

sum_int = int_1 + int_2

if sum_int > 50:
    print("Tổng 2 số lớn hơn 50!")
    print("Tổng 2 số là : " + str(sum_int))
elif sum_int < 50:
    print("Tổng 2 số bé hơn 50!")
    print("Tổng 2 số là : " + str(sum_int))