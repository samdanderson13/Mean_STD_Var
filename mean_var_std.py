import numpy as np

def calculate(a):
    calculations = dict()

    length = len(a)
    if length != 9:
        raise ValueError("List must contain nine numbers.")
    
    flattened = np.array(a)
    three_by_three = flattened.reshape((3,3))

    functions = {np.mean: 'mean', np.var: 'variance', np.std: 'standard deviation', np.max: 'max', np.min: 'min', np.sum: 'sum'}

    for fn, text in functions.items():
        val_axis1 = list(fn(three_by_three, axis=0))
        val_axis2 = list(fn(three_by_three, axis=1))
        val_flattened = fn(flattened)

        calculations[text] = [val_axis1, val_axis2, val_flattened]

    return calculations