from HinhHoc.shape import Shape
import math
class Triangle(Shape):
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        print("Chu vi hình Vuông = ",self.a + self.b + self.c)

    def area(self):
        p = (self.a + self.b + self.c)/2
        s = math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        print("Diên tích hình Vuông = ", s)

if __name__ == '__main__':
    Hinh1 = Triangle(3,4,5)
    print(Hinh1.perimeter())
    print(Hinh1.area())