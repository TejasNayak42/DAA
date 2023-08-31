def knapsack_max_profit(weights, costs, capacity):
    num_items = len(weights)
    table = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(costs[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    selected_items = []
    total_weight = capacity
    for i in range(num_items, 0, -1):
        if table[i][total_weight] != table[i - 1][total_weight]:
            selected_items.append(i - 1)
            total_weight -= weights[i - 1]

    return table[num_items][capacity], selected_items

weights = [2, 3, 5, 7, 1, 4, 1]  # weights of the coffee bean types
costs = [10, 5, 15, 7, 6, 18, 3]  # costs of the coffee bean types
capacity = 15  # maximum weight capacity of the bag

max_profit, selected_items = knapsack_max_profit(weights, costs, capacity)

print("Maximum Profit:", max_profit)
print("Selected Coffee Beans (index):", selected_items)
print("Selected Coffee Beans (weight):", [weights[i] for i in selected_items])
print("Selected Coffee Beans (cost):", [costs[i] for i in selected_items])