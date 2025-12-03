import heapq
import random

# Each item has a (name, demand score, cost)
inventory_items = [
    ("ItemA", 90, 40),
    ("ItemB", 70, 30),
    ("ItemC", 50, 20),
    ("ItemD", 60, 25),
    ("ItemE", 30, 10),
    ("ItemF", 40, 15)
]

BUDGET = 70  # Max total cost allowed


# -------- Hill Climbing Search --------
def hill_climbing(items, budget):
    current = []
    current_score = 0
    current_cost = 0

    for item in sorted(items, key=lambda x: x[1], reverse=True):  # Sort by demand
        if current_cost + item[2] <= budget:
            current.append(item)
            current_cost += item[2]
            current_score += item[1]
    return current, current_score


# -------- Best-First Search --------
def best_first_search(items, budget):
    frontier = []
    heapq.heapify(frontier)

    for item in items:
        priority = -item[1]  # Maximize demand (so we use negative)
        heapq.heappush(frontier, (priority, [item], item[1], item[2]))  # (priority, items, total_demand, total_cost)

    best_result = ([], 0)

    while frontier:
        _, current_items, demand, cost = heapq.heappop(frontier)
        if cost > budget:
            continue
        if demand > best_result[1]:
            best_result = (current_items, demand)
        for item in items:
            if item not in current_items and cost + item[2] <= budget:
                new_items = current_items + [item]
                new_demand = demand + item[1]
                new_cost = cost + item[2]
                heapq.heappush(frontier, (-new_demand, new_items, new_demand, new_cost))
    return best_result


# --------- Run Both Algorithms --------
print("Running Hill Climbing:")
selected_items_hc, score_hc = hill_climbing(inventory_items, BUDGET)
for item in selected_items_hc:
    print(item)
print("Total Demand Score:", score_hc)

print("\nRunning Best-First Search:")
selected_items_bfs, score_bfs = best_first_search(inventory_items, BUDGET)
for item in selected_items_bfs:
    print(item)
print("Total Demand Score:", score_bfs)
