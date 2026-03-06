def min_cost_assignment(cost):

    n = len(cost)
    dp = [float("inf")] * (1<<n)
    dp[0] = 0

    for mask in range(1<<n):

        worker = bin(mask).count("1")

        for task in range(n):

            if not (mask & (1<<task)):

                new_mask = mask | (1<<task)

                dp[new_mask] = min(
                    dp[new_mask],
                    dp[mask] + cost[worker][task]
                )

    return dp[(1<<n)-1]


if __name__ == "__main__":

    cost = [
        [9,2,7],
        [6,4,3],
        [5,8,1]
    ]

    print("Minimum cost:", min_cost_assignment(cost))