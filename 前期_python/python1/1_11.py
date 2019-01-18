#python 3.6.3
import numpy.random as rnd
print('数あてゲームだよぉ♡\n')

answer=rnd.randint(1,100)
counter=0
print("ランダムに正解の数を生成したよぉ♡\n")
print("ヒント：答えは1~100の間だよぉ♡")

#ゲームループ
while(True):
    hoge=int(input("答えを入力してね♡："))
    counter+=1
    if hoge<answer:
        print("ヒント：答えはもっと大きいよぉ♡\n")
    elif hoge>answer:
        print("ヒント：答えはもっと小さいよぉ♡\n")
    else:
        print("大正解！！！！！\n")
        break
#リザルト
print("最初に生成した答えは{}だったよぉ\nあなたは{}回で当てれたね♡\nすごぉーーーい！！！".format(str(answer),str(counter)))
