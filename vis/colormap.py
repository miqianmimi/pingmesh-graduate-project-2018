#!/usr/bin/env python2

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

f, ax = plt.subplots(figsize=(10, 8), dpi=500)

flights = sns.load_dataset('flights')
flights = flights.pivot('month', 'year', 'passengers')
data = np.random.rand(2000, 2000)

#cmap = sns.cubehelix_palette(start=2, rot=0.1, gamma=0.8, as_cmap=True)

sns.heatmap(data, linewidth=0, cmap='Greens_r', ax=ax)

f.savefig('a.png', bbox_inches='tight')
