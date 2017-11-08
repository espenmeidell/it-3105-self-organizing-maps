# Project: IT_3105_Module_4
# Created: 31.10.17 13:12
import numpy as np
tensor = np.array


class Utilities:
    @staticmethod
    def normalize_coordinates(cities: tensor) -> tensor:
        cities = np.copy(cities)
        means = np.mean(cities, axis=0)
        stds = np.std(cities, axis=0)
        for row in range(len(cities)):
            for col in range(1, len(cities[row])):
                cities[row][col] = (cities[row][col] - means[col]) / stds[col]
        return cities

    @staticmethod
    def euclidian_distance(v1: tensor, v2: tensor) -> float:
        assert len(v1) == len(v2), "Tensors must be of equal length to compute distance"
        return np.sqrt(np.sum(np.square(v1-v2)))

    @staticmethod
    def get_winning_neuron(case: tensor, weight_matrix: tensor) -> int:
        distances = np.apply_along_axis(Utilities.euclidian_distance, 1, weight_matrix, case)
        return int(np.argmin(distances))

    @staticmethod
    def update_weight_matrix(case: tensor, l_rate: float, win_index: int, weight_matrix: tensor):
        j = win_index
        weight_matrix[j] = weight_matrix[j] + l_rate * (case - weight_matrix[j])

    @staticmethod
    def store_tsm_result(case: int, nodes: int, l_rate: float, radius: int, decay: str, result: float):
        line = "%d\t\t%d\t\t%.2f\t\t%d\t\t%s\t\t%.2f\n" % (case, nodes, l_rate, radius, decay, result)
        with open("tsm_results.txt", "a") as f:
            f.write(line)
