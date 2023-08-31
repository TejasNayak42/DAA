def Prims(n, cost):
    selected = [0] * n
    selected[0] = 1
    for _ in range(n - 1):
        minimum, x, y = float('inf'), 0, 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j] < minimum:
                        minimum, x, y = cost[i][j], i, j
        print(x, '-->', y, ':', minimum)
        selected[y] = 1


def Kruskals(n, cost):
    parent = list(range(n))
    edges = [(i, j, cost[i][j]) for i in range(n) for j in range(i + 1, n) if cost[i][j] > 0]
    edges.sort(key=lambda x: x[2])
    mincost = 0
    for i, j, weight in edges:
        if parent[i] != parent[j]:
            mincost += weight
            print("Edge:", j + 1, "-->", i + 1, "Cost:", weight)
            parent = [parent[j] if p == parent[i] else p for p in parent]

    print("Minimum cost =", mincost)


n = int(input("Enter the number of nodes: "))
cost = [list(map(int, input().split())) for _ in range(n)]

print("Minimum Spanning Tree using Prim's Algorithm:")
Prims(n, cost)

print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
Kruskals(n, cost)

'''
0 3 99 99 6 5
3 0 1 99 99 4
99 1 0 6 99 4
99 99 6 0 8 5
6 99 99 8 0 2
5 4 4 5 2 0

'''