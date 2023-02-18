import numpy as np


def calculate(l):
    if len(l) < 9:
        raise ValueError("La lista debe contener nueve números")
    else:
        arr = np.array(l)
        matrix = arr.reshape(3,3)
        mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
        variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]
        stand_dev = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]
        max = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]
        min = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]
        sum = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
        result = {'mean': mean, 'variance': variance, 'standard deviation': stand_dev, 'max': max, 'min': min, 'sum': sum}
        return result