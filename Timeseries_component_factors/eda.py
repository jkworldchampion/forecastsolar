import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

energy = pd.read_csv("https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/energy.csv") 

print(energy.head(3), energy.tail(3)) #18년 3월, 19년, 20년, 21년 1월

