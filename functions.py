import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

penguins = sns.load_dataset("penguins")

# displot is like bar graph
# sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")

# for kernel density plot
# sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde")

g = sns.FacetGrid(penguins, col="sex", height=3.5, aspect=.75)

plt.show()