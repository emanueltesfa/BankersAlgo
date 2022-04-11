# Based on example 7.5.3.3
import numpy as np

if __name__ == '__main__':
    x = 5
    y = 3
    max = np.array([
        [7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]
    ])
    allocation = np.array([
        [0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]
    ])
    need = max - allocation
    available = np.array([3, 0, 1])
    failed = []
    rows = np.array([])

    for i in range(x):
        count = 0
        for j in range(y):
            if available[j] >= need[i][j]:
                count += 1
        if count == y:
            rows = np.append(rows, i)  # add row number to the safe sequence
            available = available + allocation[i]  # calc new available
        else:
            # print("false")
            failed.append(i)
            continue

    # checks back for failed sequences to see if new available is larger
    for a in range(len(failed)):
        count = 0
        for b in range(y):
            if available[b] >= need[failed][0][b]:  # the available is now bigger"
                count += 1
        if count == y:
            available = available + allocation[failed[0]]  # calc new available
            rows = np.append(rows, failed[0])
        else:
            print("No safe sequence found")
        if len(failed) > 1:
            failed.pop(a)
    print("Safe sequence found", rows)
    print("Available array is: \n", available, "\nNeed matrix is: \n", need)