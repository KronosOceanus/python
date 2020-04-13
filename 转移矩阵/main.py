import numpy as np


def markov(n):
    current_status = np.array([1/4, 1/4, 1/4, 1/4])
    transfer_matrix = np.array([[1/3, 1/3, 1/3, 0], [0, 0, 1/2, 1/2], [0, 1, 0, 0], [1/2, 0, 0, 1/2]])
    img_points = []
    for i in range(n):
        current_status = np.dot(current_status, transfer_matrix)
    print(current_status)


markov(5)
markov(100)
