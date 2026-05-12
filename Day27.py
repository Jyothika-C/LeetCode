# Minimum Initial Energy to Finish All Tasks

def minimum_energy(tasks):
    # Sort by (minimum - actual) descending
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

    energy = 0

    for actual, minimum in tasks:
        energy = max(energy + actual, minimum)

    return energy


# -------- User Input --------
n = int(input("Enter number of tasks: "))

tasks = []
print("Enter tasks as actual minimum pairs:")
for _ in range(n):
    a, b = map(int, input().split())
    tasks.append([a, b])

result = minimum_energy(tasks)

print("Minimum initial energy required:", result)


#sample  input
# Sample Input
# Enter number of tasks: 3
# 1 2
# 2 4
# 4 8
# 📌 Sample Output
# Minimum initial energy required: 8