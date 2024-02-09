def lunch_box_pack(menu: dict, budget: int):
    sorted_items = sorted(
        menu.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_items = []
    total_calories = 0
    for item in sorted_items:
        if budget >= item[1]["cost"]:
            total_items.append(item[0])
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
    return (
        total_items,
        total_calories,
    )


def lunch_box_pack_dp(items: dict, budget: int):
    n = len(items)
    items_list = list(items.items())

    # table
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # bottom up
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            # budget limit
            if items_list[i - 1][1]["cost"] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # max value
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items_list[i - 1][1]["cost"]]
                    + items_list[i - 1][1]["calories"],
                )

    res = dp[n][budget]
    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(items_list[i - 1][0])
            res -= items_list[i - 1][1]["calories"]
            w -= items_list[i - 1][1]["cost"]

    selected_items.reverse()

    return selected_items, dp[n][budget]


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 40
    selected_items, total_calories = lunch_box_pack(items, budget)
    print("Greedy algorithm:")
    print(f"Selected items: {selected_items}")
    print(f"Total calories: {total_calories}")

    print("Dynamic programming:")
    budget = 75
    selected_items, total_calories = lunch_box_pack_dp(items, budget)
    print(f"Selected items: {selected_items}")
    print(f"Total calories: {total_calories}")
