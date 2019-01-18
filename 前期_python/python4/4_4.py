import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def get_minimum_weight_node(weights, candidates):
    # 候補ノード番号リストcandidatesの中から，最小となる重みweights[x]を持つノード番号xを返す

    min_cand = -1
    min_weight = float('inf')

    for x in candidates:
        if(min_weight > weights[x]):

            min_cand = x
            min_weight = weights[x]

    print(candidates, min_cand, weights)

    return min_cand


def get_path_by_djikstra(matrix, start_node):
    # 隣接行列matrixによって表されるグラフ上で，始点番号start_nodeから始まる各ノードへの最短パスに含まれるエッジリストをダイクストラ法で求めて返す。

    g_size = len(matrix)

    weights = [float('inf')] * g_size # 重みリストを無限大で初期化
    selected_edges = [-1] * g_size # 接続先リストを無接続(-1)で初期化
    
    weights[start_node] = 0 # 始点ノードの重みを0にする
    next_nodes = list(range(g_size)) # 起点ノードリストを[0,1,2,…,g_size-1]で初期化

    while(next_nodes): # 起点ノードリストが空でないならば
        
        x = get_minimum_weight_node(weights, next_nodes) # 起点ノードリストから最小重みのノードを取り出す
        next_nodes.remove(x)

        for n in range(g_size):
            if(matrix[x][n] != 0):
                if(weights[n] > matrix[x][n] + weights[x]):

                    weights[n] = matrix[x][n] + weights[x] # 重みの更新
                    selected_edges[n] = [x,n] # 接続元リストをノードの組リストで更新

    for j in range(g_size):
        if(-1 in selected_edges):
            selected_edges.remove(-1)
        else:
            break

    return selected_edges

def display_graph_from_matrix(matrix, path, start_node, end_node):
    # 隣接行列を表すmatrixと色を変えたいエッジリストpath，および色を変えたい始点番号start_node，終点番号end_nodeを使って，グラフを描画する。

    adj_mat = np.asmatrix(matrix)

    G = nx.convert_matrix.from_numpy_matrix(adj_mat,create_using=nx.Graph())
    pos = nx.spring_layout(G)

    allnodes = nx.draw_networkx_nodes(G, pos, node_color='white')
    allnodes.set_edgecolor('black')
    allnodes.set_linewidth(2.0)
    tnode = nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color='orange')
    tnode.set_edgecolor('black')
    tnode.set_linewidth(2.0)
    snode = nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='orange')
    snode.set_edgecolor('white')
    snode.set_linewidth(2.0)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='blue', alpha=0.4, width=4)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()

if(__name__ == '__main__'):
    
    start_node = 0
    goal_node = 5

    mat=[
        [0,0,0,0,0,2,0,0,1,0],
        [0,0,0,2,0,0,2,0,4,3],
        [0,0,0,0,0,0,0,4,0,0],
        [0,2,0,0,3,0,0,0,0,0],
        [0,0,0,3,0,3,1,3,0,0],
        [2,0,0,0,3,0,0,2,0,3],
        [0,2,0,0,1,0,0,0,0,0],
        [0,0,4,0,3,2,0,0,0,2],
        [1,4,0,0,0,0,0,0,0,0],
        [0,3,0,0,0,3,0,2,0,0]
    ]

    print("mat"+str(mat))

    paths = get_path_by_djikstra(mat, start_node) # 最短経路を構築するパスリストを計算
    print(str(paths))
    for i in range(int(len(paths))):
        if(paths[i][0]==start_node and paths[i][1]==goal_node):
            cache=paths[i]
            paths=[[0]*8 for i in range(8)]
            paths[0]=cache
            print(str(paths))
            break
    
    display_graph_from_matrix(mat, paths, start_node, goal_node) # グラフとパスリストの表示
