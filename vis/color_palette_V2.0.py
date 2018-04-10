#from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
current_palette = sns.color_palette()
sns.palplot(current_palette)
plt.show()


current_palette = sns.color_palette("pastel")
sns.palplot(current_palette)
plt.show()

a=sns.cubehelix_palette(7,light=1.2,start=1, rot=1.5, reverse=True,as_cmap = True)
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(sns.color_palette(flatui))
plt.show()

#color = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
#vmin=0,vmax=40,robust=True
#YlGnBu #PiYG cmap="PiYG"
flatui = ["#ffc0cb", "#90eebf"]
cc=sns.diverging_palette(148, 0, s=75, l=65, n=20,center='light',as_cmap=True)
#cc=sns.cubehelix_palette(start="#ffc0cb",as_cmap=True)
bb=sns.cubehelix_palette(8, start=1, rot=0,dark=0,light=.95, reverse=True,as_cmap = True)
a=sns.cubehelix_palette(7,light=1.2,start=1, rot=1.5, reverse=True,as_cmap = True)
map=sns.color_palette("pastel")
pal = sns.dark_palette("palegreen", as_cmap=True)
pale = sns.light_palette('pink', as_cmap=True)
cmap = sns.cubehelix_palette(light=1, as_cmap=True)
pic=sns.heatmap(b,vmin=-50,vmax=60,cmap=cc,center=20,annot=True,ax=ax,linewidths=1.5, linecolor='white',annot_kws={"size":7})
for text in pic.texts:
    text.set_size(7)
    if int(text.get_text())> int(50):
        text.set_size(12)
        text.set_weight('bold')
        text.set_style('italic')
