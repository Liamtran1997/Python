# Supper Class
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showDetail(self):
        print("Account Details :" )
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)

# Sub Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    # Gửi tiền
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount # Mỗi lần call lại thì cộng thêm vào cái cũ.
        print("Số dư tài khoản đã được cập nhật : $", self.balance)
    
    # Rút tiền
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Số dư tài khoản không đủ. Xin nhập lại ! : $",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Số dư tài khoản đã được cập nhật : $", self.balance)

    def view_Balance(self):
        self.showDetail()
        print("Số tiền trong tài khoản hiện tại : $", self.balance)


ID132 = Bank("Trần Châu Tuấn",24,"Male")

ID132.deposit(100)
ID132.deposit(200)
ID132.deposit(700)

ID132.withdraw(800)

ID132.view_Balance()   