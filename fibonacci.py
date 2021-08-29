# Nhập vào 1 số 

def my_fibonaccia(n):
    if n < 2:
        return 1    
    else:
        f0 = 0
        f1 = 1
        fn = 0
        while n >= 2: 
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n -= 1
        return fn
n = -1
while n < 0:
    n = int(input("Nhập số tự nhiên N : "))
    if n >= 0:
        break

result = my_fibonaccia(n)
print("Kết quả = "+str(result))
