def knapsack(wt,val,N,W):
    sol,selected=[[0]*(W+1) for _ in range(N+1)],[0]*(N+1)
    for i in range(1,N+1):
        for j in range(1,W+1):
            sol[i][j]=sol[i-1][j] if wt[i]>j else max(sol[i-1][j],sol[i-1][j-wt[i]]+val[i])
    i,j=N,W
    while i>0 and j>0:
        if sol[i][j]!=sol[i-1][j]:
            selected[i],j=1,j-wt[i]
        i-=1
    print("\nThe Optimal Solution is:",sol[N][W])
    print("Items selected are:",", ".join(map(str,[i for i in range(N+1) if selected[i]])))
N=int(input("Enter the number of items: "))
wt=[0]+list(map(int,input(f"Enter the weights of {N} items: ").split()))
val=[0]+list(map(int,input(f"Enter the values of {N} items: ").split()))
W=int(input("Enter the Knapsack Capacity: "))
knapsack(wt,val,N,W)
