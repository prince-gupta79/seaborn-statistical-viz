import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

tips = sns.load_dataset("tips")

# sns.displot(data=tips, x="total_bill", col="time", kde=True)

sns.displot(data=tips, x="total_bill", col="time", hue="smoker", rug=True)

# For Categorical data
# sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

plt.show()

