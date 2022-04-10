# Based on example 7.5.3.3
import numpy as np

if __name__ == '__main__':
    x = 5
    y = 4
    max = np.array([
        [0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]
    ])
    allocation = np.array([
        [0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]
    ])
    need = max - allocation
    available = np.array([1, 5, 2, 0])
    failed = np.array([])
    # available = np.array([0, 0, 0, 0])
    # newAvailable = np.array([])

    for i in range(x):
        count = 0
        for j in range(y):
            # print(available[j]
            # print(available[j], need[i][j])
            if available[j] >= need[i][j]:
                count += 1
        # print(count, " is the count")
        if count == y:
            # calc new available
            print(f"Row P{i + 1} is apart of the safe sequence")
            available = available + allocation[i]
        else:
            print("false")
            failed = [i]
            continue

    # need[failed][0][1]
    need[failed][0].append(1, 9)
    print(need[failed][0])
    for a in range(len(failed)):
        for b in range(i):
            for c in range(j):
                # print("Available, ", available[b], "Failed Need", need[failed][0][b])
                print("Available, ", available, "Failed Need", need[failed][0])

                if available[b] >= need[0][b]:
                    print("the availible is now bigger")
                else:
                    print("No safe sequence found")
                #     print("Failed", need[failed])
                # failed.pop()

    # print("Available array is: \n", available, "\nNeed matrix is: \n", need)