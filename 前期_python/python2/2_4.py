def fibonacci_rec(n):
    #nが0位上のint型と過程してnのフィボナッチ数を返す
    if n<=1:
        return 1
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)

for i in range(31):
    key_input=input("int型のn(0<=n<=30)を指定して下さい：")
    print(fibonacci_rec(int(key_input)))

