import numpy as np

def calculate(list1):
    if(len(list1) < 9):
        raise ValueError("List must contain nine numbers.")
    flat = np.array(list1)
    mat = flat.copy()
    mat.resize((3,3))
    # print(flat)
    # print(mat)
    calculations = {}
    mean_arr = [mat.mean(axis=0).tolist(),mat.mean(axis=1).tolist(), flat.mean().tolist()]
    var_arr = [mat.var(axis=0).tolist(),mat.var(axis=1).tolist(), flat.var().tolist()]
    stdd_arr = [mat.std(axis=0).tolist(),mat.std(axis=1).tolist(), flat.std().tolist()]
    max_arr = [mat.max(axis=0).tolist(),mat.max(axis=1).tolist(), flat.max().tolist()]
    min_arr = [mat.min(axis=0).tolist(),mat.min(axis=1).tolist(), flat.min().tolist()]
    sum_arr = [mat.sum(axis=0).tolist(),mat.sum(axis=1).tolist(), flat.sum().tolist()]
    calculations["mean"] = mean_arr
    calculations["variance"] = var_arr
    calculations["standard deviation"] = stdd_arr
    calculations["max"] = max_arr
    calculations["min"] = min_arr
    calculations["sum"] = sum_arr
    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))