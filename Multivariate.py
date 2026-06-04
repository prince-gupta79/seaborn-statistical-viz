import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

penguins = sns.load_dataset("penguins")

#sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

# Pairplot is for brorder data
# sns.pairplot(data=penguins, hue="species")

g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))

plt.show()

# Its amazing..... 