QUEEN = 9
EMPTY = 0

def print_grids(grids):
    #盤面の2次元配列gridsを表示する

    for row in grids:
        print(row)
    
    print()

def is_free_anti_diagonal(grids,y,x):
    #盤面gridsの座標(y,x)を基準として反対書く方向にクイーンが配置されていないならTrueを返す

    for i in range(8+1):

        if(y-i>=0 and x+i<8+1):
            if(grids[y-i][x+i]!=0):
                return False
        
        if(y+i<8+1 and x-i>=0):
            if(grids[y+1][x-i]!=0):
                return False
    
    return True

def is_free_diagonal(grids,y,x):
    #盤面gridsの座標(x,y)を基準として対角方向にクイーンが配置されていないならTrueを返す

    for i in range(8+1):

        if(y-i>=0 and x-i>=0):
            if(grids[y-i][x-i]!=0):
                return False

        if(y+i<8+1 and x+i<8+1):
            if(grids[y+i][x+i]!=0):
                return False
    
    return True

def is_free_column(grids,x):
    #盤面gridsのx座標を基準として列方向にクイーンが配置されていないならTrueを返す

    for j in range(8+1):
        if(grids[j][x]!=EMPTY):
            return False
    
    return True

def is_free(grids,y,x):
    #盤面gridsの座標(x,y)にクイーンが配置できるならTrueを返す

    if(is_free_column(grids,x) and is_free_diagonal(grids,y,x) and is_free_anti_diagonal(grids,y,x)):

        return True
    else:
        return False

i=0

def find_eight_queen(grids,y):
    global i
    #盤面gridsのy座標を基準として行方向にクイーンが配置できる場所を探す

    for x in range (8):
        if(is_free(grids,y,x)):
            grids[y][x]=QUEEN

            if(y==(8-1)):
                i=i+1
                # print('{}枚目'.format(i))
                # print_grids(grids)
            else:
                find_eight_queen(grids,y+1)

            grids[y][x]=EMPTY
    return

def create_grids(n):
    #n*nサイズの初期盤面を返す

    grids=[]

    for _ in range(n):
        column=[]

        for _ in range(n):
            column.append(0)

        grids.append(column)
    return grids

if __name__ == '__main__':
    grids = create_grids(8+1)
    find_eight_queen(grids,0)
    print('正答盤面の総数：{}'.format(i))

