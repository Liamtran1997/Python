class Money():
    def __init__(self, id, exchange_rate
    , quantity, currency):
        self.id = id
        self.exchange_rate = exchange_rate
        self.quantity = quantity
        self.currency = currency
    

    def show_Detail(self):
        print("Thông tin giao dịch Ngoại Tệ :")
        print("Mã giao dịch : ", self.id)
        print("Tỷ giá giá : ", self.exchange_rate)
        print("Số lượng : ", self.quantity)
        print("Loại Tiền Tệ : ", self.currency)

    def buying(self):
        return print("Giá mua là : ", self.quantity*self.exchange_rate)

    def selling(self):
        return print("Giá bán là : ", (self.quantity*self.exchange_rate)*1.05)

if __name__ == '__main__':
    usd = Money("MN1",23000,20,"USD")
    aud = Money("MN2",17300,10,"AUD")
    eur = Money("MN3",16500,50,"EUR")
    print(usd.show_Detail())
    print(usd.buying())
    print(usd.selling())