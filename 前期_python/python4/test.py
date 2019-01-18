foo=1
bar=8

hoge = [
    [8, 0], 
    [7, 2],
    [1, 3],
    [6, 4],
    [4, 5],
    [1, 6],
    [9, 7],
    [1, 8],
    [1, 9]
]

for k in range(int(len(hoge))):
    print("die"+str(hoge[k]))
    if(hoge[k][0]==foo and hoge[k][1]==bar):
        fuck=[[0]*int(len(hoge)) for b in range(int(len(hoge)))]
        fuck[0]=hoge[k]
        print('fuck you'+str(fuck))

