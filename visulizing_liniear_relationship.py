import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://www.instagram.com/nomanionholiday/", encoding = 'latin1')
data = data.dropno()
print(data.head())