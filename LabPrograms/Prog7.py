class Sales:
    def __init__(self):
        self.cost, self.a, self.visit = 0, [[0] * 100 for _ in range(100)], [0] * 100
    def mincost(self, c, n):
        self.visit[c] = 1
        print(c, "-->", end="")
        ncity = self.nearest(c, n)
        if ncity == 999:
            print(1)
            self.cost += self.a[c][1]
            return
        self.mincost(ncity, n)
    def nearest(self, c, n):
        nc, min_val, kmin = 999, 999, 999
        for i in range(1, n + 1):
            if self.a[c][i] and not self.visit[i]:
                if self.a[c][i] < min_val:
                    min_val, kmin, nc = self.a[i][1] + self.a[c][i], self.a[c][i], i
        if min_val != 999:
            self.cost += kmin
        return nc
x = Sales()
n = int(input("Enter the Number of cities: "))
print("Enter the Cost Matrix: ")
for i in range(1, n + 1):
    x.a[i][1:n+1] = map(int, input().split())
print("The Cost Matrix is:")
for i in range(1, n + 1):
    print(" ".join(map(str, x.a[i][1:n+1])))
print("Optimal solution:\nThe path is:")
x.mincost(1, n)
print("Minimum cost is:", x.cost)
