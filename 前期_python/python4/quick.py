def quick_sort(arr):
    hidari = []
    migi = []
    if len(arr) <= 1:
        return arr
    
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            hidari.append(ele)
        elif ele > ref:
            migi.append(ele)
        else:
            ref_count += 1
    hidari = quick_sort(hidari)
    migi = quick_sort(migi)
    return hidari + [ref] * ref_count + migi

arr = [3,2,5,1,4]
print(str(arr))

arr = quick_sort(arr)
print(str(arr))
