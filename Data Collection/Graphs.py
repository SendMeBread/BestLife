import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
data = {'Lap':[1, 2, 3, 4, 5],'Avg':[174.86, 172.49, 175.14, 170.92, 168.28]}
df = pd.DataFrame(data)
sns.relplot(data=df, x="Lap", y="Avg", kind="line")
