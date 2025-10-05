import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list, dtype=float)
    arr1 = arr.reshape((3, 3))
    

    stat = {
        "mean": [
            [np.mean(arr1[:,0]).item(), np.mean(arr1[:,1]).item(), np.mean(arr1[:,2]).item()],
            [np.mean(arr1[0,:]).item(), np.mean(arr1[1,:]).item(), np.mean(arr1[2,:]).item()],
            np.mean(arr1).item()
        ],
        "variance": [
            [np.var(arr1[:,0]).item(), np.var(arr1[:,1]).item(), np.var(arr1[:,2]).item()],
            [np.var(arr1[0,:]).item(), np.var(arr1[1,:]).item(), np.var(arr1[2,:]).item()],
            np.var(arr1).item()
        ],
        "standard deviation": [
            [np.std(arr1[:,0]).item(), np.std(arr1[:,1]).item(), np.std(arr1[:,2]).item()],
            [np.std(arr1[0,:]).item(), np.std(arr1[1,:]).item(), np.std(arr1[2,:]).item()],
            np.std(arr1).item()
        ],
        "max": [
            [np.max(arr1[:,0]).item(), np.max(arr1[:,1]).item(), np.max(arr1[:,2]).item()],
            [np.max(arr1[0,:]).item(), np.max(arr1[1,:]).item(), np.max(arr1[2,:]).item()],
            np.max(arr1).item()
        ],
        "min": [
            [np.min(arr1[:,0]).item(), np.min(arr1[:,1]).item(), np.min(arr1[:,2]).item()],
            [np.min(arr1[0,:]).item(), np.min(arr1[1,:]).item(), np.min(arr1[2,:]).item()],
            np.min(arr1).item()
        ],
        "sum": [
            [np.sum(arr1[:,0]).item(), np.sum(arr1[:,1]).item(), np.sum(arr1[:,2]).item()],
            [np.sum(arr1[0,:]).item(), np.sum(arr1[1,:]).item(), np.sum(arr1[2,:]).item()],
            np.sum(arr1).item()
        ]
    }

    return stat