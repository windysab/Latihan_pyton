import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
table = pd.read_csv("dataset.csv")
table.head()

# Define the labels and colors
x_label = table['NAMA KELURAHAN']
colors = ['red', 'blue', 'green', 'purple', 'orange']

# Create the bar plot with different colors
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'], color=colors, tick_label=x_label)
plt.xlabel('NAMA KELURAHAN')
plt.ylabel('LAKI-LAKI WNI')
plt.title('Jumlah Laki-Laki WNI per Kelurahan')
plt.show()