import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid", color_codes = True)
sns.set(font_scale = 1)

flats = pd.read_csv("albert.csv")
print(flats.head())
#Shape command will give number of rows and number of of columns in dataset
print(flats.shape)
#Describe gives statistical information about numerical columns in the dataset
print(flats.describe())

corr = flats.corr()["Price per month"]
print(corr[np.argsort(corr,axis = 0)[:: -1]])

#plotting correlations
num_feat = flats.columns[flats.dtypes!=object]
num_feat = num_feat[1:-1]
labels = []
values = []
for col in num_feat:
	labels.append(col)
	values.append(np.corrcoef(flats[col].values, flats["Price per month"].values)[0,1])

ind = np.arange(len(labels))
width = 0.9
fig, ax = plt.subplots(figsize = (12,12))
rexts = ax.barh(ind, np.array(values), color = "red")
ax.set_yticks(ind+((width)/2.))
ax.set_yticklabels(labels, rotation = "horizontal")
ax.set_xlabel("Correlation coefficient")
ax.set_title("Correlation Coefficients w.r.t Sale Price")

plt.show()