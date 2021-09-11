
from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def tinh_chu_vi(self):
        return (self.length + self.width)*2
    
    def tinh_dien_tich(self):
        return (self.length* self.width)

if __name__ == '__main__':
    Hinh2 = Rectangle(2,3)
    print("Chieu dai hinh chu nhat: ", Hinh2.length)
    print("Chieu rong hinh chu nhat: ", Hinh2.width)
    print("Chu vi hinh tron: ", Hinh2.tinh_chu_vi())
    print("Dien tich hinh tron: ", Hinh2.tinh_dien_tich())