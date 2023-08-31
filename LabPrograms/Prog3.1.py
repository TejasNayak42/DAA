def dij(n, v, cost):
    flag, dist, path = [0] * (n + 2), [float('inf')] * (n + 2), [[] for _ in range(n + 2)]
    dist[v], path[v] = 0, [v]

    for _ in range(n):
        i, min_dist = -1, float('inf')
        for j in range(1, n + 1):
            if not flag[j] and dist[j] < min_dist: i, min_dist = j, dist[j]

        if i == -1: break
        flag[i] = 1

        for j in range(1, n + 1):
            if dist[i] + cost[i][j] < dist[j]:
                dist[j], path[j] = dist[i] + cost[i][j], path[i] + [j]

    return dist, path


n = int(input("Enter the number of vertices: "))
print("Enter the Weighted Matrix (Separated by Spaces):")
cost = [[float('inf')] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    cost[i][1:n + 1] = map(int, input().split())

v = int(input("Enter the Source Vertex: "))
dist, path = dij(n, v, cost)
print("Shortest paths from Source Vertex", v, "to the remaining vertices:")
for i in range(1, n + 1):
    if i != v: print(v, "-->", " --> ".join(map(str, path[i][1:])), "=", dist[i])
