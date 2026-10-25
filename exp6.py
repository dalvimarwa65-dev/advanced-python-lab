# 1. Top-Down Approach (Recursion with Memoization)
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def helper(i, w):
        if i == 0 or w == 0:
            return 0
        
        if (i, w) in memo:
            return memo[(i, w)]
        
        # If item weight exceeds current capacity, skip it
        if weights[i-1] > w:
            memo[(i, w)] = helper(i-1, w)
        else:
            # Max of including vs excluding the current item
            include = values[i-1] + helper(i-1, w - weights[i-1])
            exclude = helper(i-1, w)
            memo[(i, w)] = max(include, exclude)
            
        return memo[(i, w)]

    return helper(n, capacity)


# 2. Bottom-Up Approach (Dynamic Programming Tabulation)
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP array with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# --- Example Usage ---
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print("Top-Down Approach Result:")
    print("Maximum Value:", knapsack_top_down(weights, values, capacity))

    print("\nBottom-Up Approach Result:")
    print("Maximum Value:", knapsack_bottom_up(weights, values, capacity))