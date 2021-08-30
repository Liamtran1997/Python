# Tính công thức các hình khối 

def hinh_vuong(a):
    chu_vi = a * 4
    dien_tich = a * a
    print("Chu vi hình vuông = " + str(chu_vi))
    print("Diện tích hình vuông = " + str(dien_tich))

hinh_vuong(5)


# Cách 2
def chu_nhat(width, height):
    chu_vi = (width + height) * 2
    dien_tich = width * height
    return chu_vi, dien_tich

width = 4
height = 7
chu_vi, dien_tich = chu_nhat(width, height)
print("Chu vi hình Chử Nhật = " + str(chu_vi))
print("Diện tích hình Chử Nhật = " + str(dien_tich))