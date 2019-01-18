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
