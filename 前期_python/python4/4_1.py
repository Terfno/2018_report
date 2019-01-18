def sort_by_bubble(lst):
    # リストlstを昇順でバブルソートによってソートする

    list_size=len(lst)
    for j in range (list_size):
        for i in range (list_size-j-1):
            if(lst[i]>lst[i+1]):
                s=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=s
    
    return lst

# 使用する

## テスト用の配列hoge_list
hoge_list=[3,2,5,1,4]

## sort_by_bubble使用，表示
hoge_bubble=sort_by_bubble(hoge_list)
print("sort_by_bubble:"+str(hoge_bubble))

## チェック用にsortedメソッドを用いてソート，ソート結果をhoge_sortedに格納→表示
hoge_sorted=sorted(hoge_list)
print("sorted():"+str(hoge_sorted))
