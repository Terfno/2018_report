# 第一回 Pythonによるプログラミング
* 実験年月日 2018年5月21日
* 提出年月日 2018年5月__日
* 班番号 6
* 報告者 3年19番6班 末田 貴一
* 共同実験者
    * 7番 川上 求
    * 42番 山崎 敦史
    * 47番 ロンサン
## 問題1.1
### ソースコード
```
import numpy
numpy.cos(2*numpy.pi)
numpy.sin(0)
numpy.tan(numpy.pi/2)
quit()

```
### 実行結果
```
$>python -i
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.cos(2*numpy.pi)
1.0
>>> numpy.sin(0)
0.0
>>> numpy.tan(numpy.pi/2)
16331239353195370.0
>>> quit()
$>
```
## 問題1.2
### ソースコード
```
s="ほげ"
str(1)
str(3.14159265)
str(False)
str(0.7+14.135j)
int('0')
float('2.7')
bool('True')
complex('2+1j')

'すえだ'+'たかひと'
'ばーか'*2

'huga'=="huga"
'hoge'in'huga'
'huga'!='hoge'
'huga'not in'piyo'

quit()

```
### 実行結果
```
$>python -i
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> s="ほげ"
>>> str(1)
'1'
>>> str(3.14159265)
'3.14159265'
>>> str(False)
'False'
>>> str(0.7+14.135j)
'(0.7+14.135j)'
>>> int('0')
0
>>> float('2.7')
2.7
>>> bool('True')
True
>>> complex('2+1j')
(2+1j)
>>>
>>> 'すえだ'+'たかひと'
'すえだたかひと'
>>> 'ばーか'*2
'ばーかばーか'
>>>
>>> 'huga'=="huga"
True
>>> 'hoge'in'huga'
False
>>> 'huga'!='hoge'
True
>>> 'huga'not in'piyo'
True
>>>
>>> quit()
$>
```
## 問題1.3
### ソースコード
```
lst=[1,2,3]
lst[1]
lst[1]=4
lst
len(lst)
list("hello world")

lst=[]
lst.append(5)
lst.append('hello')
lst

lst=[]
lst.append(6)
lst.append('world')
lst.remove('world')
lst

lst=[7,8,9]
lst.clear()
lst

[10,'11']+[12,13]
[14]*15

[16,17]==[16,17]
[16,17]!=[18,19]
19 in [18,19]
19 not in [18,19]

quit()

```
### 実行結果
```
$>python -i
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> lst=[1,2,3]
>>> lst[1]
2
>>> lst[1]=4
>>> lst
[1, 4, 3]
>>> len(lst)
3
>>> list("hello world")
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>>
>>> lst=[]
>>> lst.append(5)
>>> lst.append('hello')
>>> lst
[5, 'hello']
>>>
>>> lst=[]
>>> lst.append(6)
>>> lst.append('world')
>>> lst.remove('world')
>>> lst
[6]
>>>
>>> lst=[7,8,9]
>>> lst.clear()
>>> lst
[]
>>>
>>> [10,'11']+[12,13]
[10, '11', 12, 13]
>>> [14]*15
[14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
>>>
>>> [16,17]==[16,17]
True
>>> [16,17]!=[18,19]
True
>>> 19 in [18,19]
True
>>> 19 not in [18,19]
False
>>>
>>> quit()
$>
```
## 問題1.4
### ソースコード
```
input_str=input('x?: ')

x=input_str.split(' ')
print('二列目の要素：{}'.format(x[1]))
quit()

```
### 実行結果
```
$>python .\1_4.py
x?: hoge huga piyo
二列目の要素：huga
$>
```
## 問題1.5
### ソースコード
```
x=0
if x>0:
    print('正')
elif x<0 :
    print('負')
else:
    print('零')

quit()

```
### 実行結果
```
$>python .\1_5.py
零
$>
```
## 問題1.6
### ソースコード
```
suji1=input('1つ目の数字：')
suji2=input('2つ目の数字：')
print('足し算なら”+”を，引き算なら"-"を，掛け算なら"*"を，割り算なら”/”を指定して下さい\n')
keisan=input('四則演算の指定：')
suji1=int(suji1)
suji2=int(suji2)
if keisan=='+':
    output=suji1+suji2
    suji1=str(suji1)
    suji2=str(suji2)
    output=str(output)
    print(suji1+'+'+suji2+'='+output)
elif keisan=='-':
    output=suji1-suji2
    suji1=str(suji1)
    suji2=str(suji2)
    output=str(output)
    print(suji1+'-'+suji2+'='+output)
elif keisan=='*':
    output=suji1*suji2
    suji1=str(suji1)
    suji2=str(suji2)
    output=str(output)
    print(suji1+'*'+suji2+'='+output)
elif keisan=='/':
    output=suji1/suji2
    suji1=str(suji1)
    suji2=str(suji2)
    output=str(output)
    print(suji1+'/'+suji2+'='+output)
else:
    print('Error')
quit()

```
### 実行結果
```
$> python .\1_6.py
1つ目の数字：1
2つ目の数字：1
足し算なら”+”を，引き算なら"-"を，掛け算なら"*"を，割り算なら”/”を指定して下さい

四則演算の指定：+
1+1=2
$> python .\1_6.py
1つ目の数字：1
2つ目の数字：1
足し算なら”+”を，引き算なら"-"を，掛け算なら"*"を，割り算なら”/”を指定して下さい

四則演算の指定：-
1-1=0
$> python .\1_6.py
1つ目の数字：1
2つ目の数字：1
足し算なら”+”を，引き算なら"-"を，掛け算なら"*"を，割り算なら”/”を指定して下さい

四則演算の指定：*
1*1=1
$> python .\1_6.py
1つ目の数字：1
2つ目の数字：1
足し算なら”+”を，引き算なら"-"を，掛け算なら"*"を，割り算なら”/”を指定して下さい

四則演算の指定：/
1/1=1.0
$> 
```
## 問題1.7
### ソースコード
```
# for 変数 in range(始まりの数値, 最後の数値, 増加する量):
    #ループ処理

print('図1.12')
for i in range(5):
    print(i)

print('図1.13')
for i in range(2,4):
    print(i)

print('図1.14')
for i in range(5,1,-2):
    print(i)

print('図1.15')
lst=list('python')
for c in lst:
    print(c)

quit()

```
### 実行結果
```
$> python .\1_7.py
図1.12
0
1
2
3
4
図1.13
2
3
図1.14
5
3
図1.15
p
y
t
h
o
n
$>
```
## 問題1.8
### ソースコード
```
#図1.16
x=5
ans=0
i=x
while i>0:
    ans=ans+x
    i=i-1

print(ans)


#図1.17
x=1
while True:
    if x%11 == 0 and x % 17 == 0:
        break
    x=x+1

print(x)

```
### 実行結果
```
$> python .\1_8.py
25
187
$>
```
## 問題1.9
### ソースコード
```
def changeFirst(xs):
    xs[0]=1

lst=[0,1,2]

print(lst)

changeFirst(lst)
print(lst)

```
### 実行結果
```
$> python .\1_9.py
[0, 1, 2]
[1, 1, 2]
$>
```
## 問題1.10
### ソースコード
```
def main():
    print('Hello,World.')

if __name__ == '__main__':
    main()

```
### 実行結果
```
$>python .\1_10.py
Hello,World.
```
## 問題1.11
### ソースコード
```
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

```
### 実行結果
```
$> python .\1_11.py
数あてゲームだよぉ♡

ランダムに正解の数を生成したよぉ♡

ヒント：答えは1~100の間だよぉ♡
答えを入力してね♡：50
ヒント：答えはもっと大きいよぉ♡

答えを入力してね♡：75
ヒント：答えはもっと小さいよぉ♡

答えを入力してね♡：65
ヒント：答えはもっと小さいよぉ♡

答えを入力してね♡：55
ヒント：答えはもっと小さいよぉ♡

答えを入力してね♡：53
大正解！！！！！

最初に生成した答えは53だったよぉ
あなたは5回で当てれたね♡
すごぉーーーい！！！
$>
```
## レポート課題1.1
コンパイラとインタプリタ，それぞれを使って作ったプログラムのメリット，デメリットを調べて書け
### コンパイラのメリット デメリット
ソースを一旦機械語に翻訳→実行するタイプの言語
メリット：実行速度が速いこと
デメリット：コンパイルする手間が必要なこと，他環境で実行できない可能性があること
### インタプリタのメリット デメリット
命令を1つずつ機械語に翻訳→実行するタイプの言語
メリット：コードをすぐに実行できること
デメリット：実行速度が遅いこと
## レポート課題1.2
静的型付けプログラミング言語と動的型付けプログラミング言語のメリット，デメリットを調べて書け
### 静的型付けプログラミング言語のメリット デメリット
静的型付け＝コンパイル時に型を検査する
C言語やJavaがそう
メリット：コンパイル時に検査するのでコードが堅牢，複数人で開発する際の型付けに関するヒューマンエラーを減らせる
デメリット：書くのが面倒くさい＝コードが長くなってしまう．
### 動的型付けプログラミング言語のメリット デメリット
動的型付け＝実行時に型を検査する
RubyやPython，JavaScriptがそう
メリット：型の定義を省略できるので速く，シンプルで自由なコードが書ける
デメリット：実行時に検査するので型付けに関するヒューマンエラーが出やすくなる可能性がある
## url
https://hackmd.io/s/BkIDitk17