import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

n = 20 # data size
df = pd.DataFrame({
    "x": np.random.normal(0, 1, n),
    "y": np.random.normal(0, 1, n),
})
color = np.arctan2(df["y"], df["x"])
df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5, cmap="rainbow")
plt.show()