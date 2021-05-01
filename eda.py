import pandas as pd
import matplotlib.pyplot as plt

energy = pd.read_csv("./contest/energy.csv")
energy.head()

plt.hist(energy)
