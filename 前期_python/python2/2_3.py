def factorial_rec(n):
    #nが1以上のint型と家庭してnの階乗を返す
    if n==1:
        return 1
    else:
        return n * factorial_rec(n-1)

for i in range(10):
    key_input=input("int型のn(1<=n<=10)を指定して下さい：")
    print(factorial_rec(int(key_input)))

