import sys
import matplotlib
matplotlib.use('Agg')  # Keep this to use a non-GUI backend that allows saving plots

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Duration"].plot(kind = 'hist')

# plt.show()  # Comment or remove this if you're saving the file and not displaying it

plt.savefig('plot.png')  # Save the plot as a PNG file
sys.stdout.flush()  # This can be kept or removed, as it's not necessary for saving the file