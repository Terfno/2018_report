"""N Queen: taking symmetry into account"""

import sys



def comb(f1, f2):
    """2 つの 関数 を   合成 した 関数 を   返す """
    return lambda x:f1(f2(x))


# 対称 操作
REV  = lambda ls: list(reversed(ls))                            # 左右反転
USD  = lambda ls: [ len(ls)-x-1 for x in ls ]                   # 上下 反転
T90  = lambda ls: [ ls.index(x) for x in range(len(ls)) ]       # 90 度 回転
T180 = comb(USD, REV)                                           # 180 度 回転
T270 = comb(T90, T180)                                          # 270 度 回転
D1   = comb(REV, T90)                                           # 対角線 での 反転 その 1
D2   = comb(USD, T90)                                           # 対角線 での 反転 その 2




def is_different(cols, sols):
    """ 対称性 を  考慮し ても 固有 の 解か """
    return all( tuple(op(cols)) not in sols for op in (REV, USD, T90, T180, T270, D1, D2) )




def queen_ok(ls, row1):
    """row1 が ls にある queen と 利き が 重な らないとき True を   返す """
    return all( abs(row1-row)!=col+1  for col, row in enumerate(ls) )




def nqueen(n):
    """n x n マス の N-Queen パズル を   解く """

    def qiter(cols, rows):
        
        if rows:
            for i in rows:
                if queen_ok(cols, i):
                    qiter( (i,)+cols, rows-{i})
        elif is_different(cols, sols):
            sols.add(cols)


    sols=set()
    qiter(tuple(), frozenset(range(n)))
    return sols





if __name__=='__main__':
    sols=nqueen(int(sys.argv[1]))
    print ('N of solutions:', len(sols))
    for sol in sols:
        print (sol)