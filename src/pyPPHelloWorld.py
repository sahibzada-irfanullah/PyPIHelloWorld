
import numpy as np

import pandas as pd
df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
def add(a, b):
    print("Calling addition")
    return a + b

def sub(a, b):
    print("calling subtraction")
    return a - b

def mul(a, b):
    print("Calling multiplication")
    return a * b

def quicktext():
    print('Hello, welcome to QuickSample package.')

