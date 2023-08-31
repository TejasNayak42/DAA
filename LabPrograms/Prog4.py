maxi = 9999999
n = int(input("Enter the number of nodes: "))
selected = [False for i in range(n)]
parent = [0 for i in range(n)]
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
def uni(i, j):
    x = find(i)
    y = find(j)
    parent[x] = y
def prim_mst(n, cost):
    n_edge = 0
    selected[0] = True
    while n_edge < n - 1:
        minimum = maxi
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j]:
                        if minimum > cost[i][j]:
                            minimum = cost[i][j]
                            x = i
                            y = j
        print(x, '-->', y, ':', cost[x][y])
        selected[y] = True
        n_edge += 1
def kruskal_mst(n, cost):
    mincost = 0
    for i in range(n):
        parent[i] = i
    e_ctr = 0
    while e_ctr < n - 1:
        mini = maxi
        a = b = 0
        for i in range(n):
            for j in range(n):
                if cost[i][j] <= mini and find(i) != find(j):
                    mini = cost[i][j]
                    a = i
                    b = j
        uni(a, b)
        print("Edge", e_ctr + 1, ": (", a + 1, ",", b + 1, ") cost:", mini)
        e_ctr += 1
        mincost += mini
    print("Minimum cost =", mincost)
cost = [[int(x) for x in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if cost[i][j] == 0:
            cost[i][j] = maxi
print("Minimum Spanning Tree using Prim's Algorithm:")
prim_mst(n, cost)
print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
kruskal_mst(n, cost)
