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
    rows = np.array([])

    for i in range(x):
        count = 0
        for j in range(y):
            if available[j] >= need[i][j]:
                count += 1
        if count == y:

            rows = np.append(rows, i) # add row number to the safe sequence
            available = available + allocation[i] # calc new available
        else:
            # print("false")
            failed = [i]
            continue

    count = 0
    for a in range(len(failed)):
        for b in range(i):
            if available[b] >= need[failed][0][b]: # the available is now bigger"
                count += 1
        if count == y:
            rows = np.append(rows, failed)
            print("Safe sequence found", rows)
        else:
            print(count, y)
            print("No safe sequence found")
            #     print("Failed", need[failed])
        failed.pop()

    print("Available array is: \n", available, "\nNeed matrix is: \n", need)
