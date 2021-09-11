
class Gold:
    def __init__(self, id, unit_price
    , quantity, types_of_gold):
        self.id = id
        self.unit_price = unit_price
        self.quantity = quantity
        self.types_of_god = types_of_gold

    def show(self):
        print("Thành tiền : ", self.quantity*self.unit_price)

    def show_Detail(self):
        print("Thông tin giao dịch Vàng :")
        print("Mã giao dịch : ", self.id)
        print("Đơn giá : ", self.unit_price)
        print("Số lượng : ", self.quantity)
        print("Loại Vàng : ", self.types_of_god)

if __name__ == '__main__':
    k18 = Gold("AB1",5000,4,"18K")
    k24 = Gold("AB1",9000,4,"24K")
    k9999 = Gold("AB1",15000,4,"9999")
    print(k18.show_Detail())
    print(k18.show())

