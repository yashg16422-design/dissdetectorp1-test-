import numpy as np
import pandas as pd

def generate(samples=5000, features=5):
    base = np.random.normal(0, 1, (samples, features))
    drift = np.linspace(0, 3, samples).reshape(-1, 1)
    data = base + drift * 0.05
    return pd.DataFrame(data, columns=[f"v{i}" for i in range(features)])

if __name__ == "__main__":
    df = generate()
    df.to_csv("sample.csv", index=False)