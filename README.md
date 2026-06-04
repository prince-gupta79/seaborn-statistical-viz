seaborn-statistical-viz :

Learning seaborn for statistical data visualization — this folder covers everything from basic relational plots to advanced multivariate analysis with PairGrids and KDE contours.
Seaborn sits on top of matplotlib but makes statistical visualization significantly easier and more powerful. This is where visualization stopped feeling like a chore and started feeling useful.

## What's covered

- Relational plots — `relplot` with hue, style, size, faceting
- Distribution plots — `displot` with KDE, rug plots, histogram
- Categorical plots — `catplot` with swarm plots
- Statistical estimation — confidence intervals on line plots
- Multivariate analysis — `jointplot`, `pairplot`, `PairGrid`
- FacetGrid for multi-panel figures
- Working with real built-in datasets — tips, penguins, fmri, dots

## Files

| File | What it does |
|---|---|
| `Getting_started.py` | First seaborn plot — relplot with multiple visual dimensions |
| `statistical_etm.py` | fMRI brain signal data — line plots with confidence intervals by region |
| `dots.py` | Neural firing rate data — line plot with coherence levels and style |
| `distributional.py` | Distribution plots with KDE, rug plots, faceted by time and smoker |
| `functions.py` | FacetGrid setup, displot vs KDE comparison |
| `Multivariate.py` | PairGrid with KDE co

The interesting part ;
The datasets seaborn uses by default are more interesting than they look:

fmri — actual brain imaging signal data by region and event type
dots — neural firing rates and coherence from neuroscience research
penguins — biological morphology measurements by species
tips — real restaurant transaction data

Without realising it, this folder ended up being an introduction to biomedical data visualization; the same kind of data that shows up in healthcare AI and medical research.

Sample visualizations
fMRI brain signal analysis (statistical_etm.py)

Line plots with confidence intervals showing signal strength by brain region and event type

Neural firing rate analysis (dots.py)

Multi-panel line plots showing firing rate over time with coherence and choice dimensions

Penguin species multivariate analysis (Multivariate.py)

PairGrid combining KDE contour plots, scatter plots, and histogram diagonals across all features


Stack :
Python, seaborn, matplotlib, pandas, numpy

Setup :
bashgit clone https://github.com/prince-gupta79/seaborn-statistical-viz.git
cd seaborn-statistical-viz
pip install seaborn matplotlib pandas numpy
Then run any file:
bashpython Getting_started.py

Why I built this
After learning matplotlib from scratch, seaborn felt like a significant upgrade for statistical work. The ability to encode multiple dimensions of data — hue, style, size, facets — into a single clean chart is genuinely powerful.
The multivariate analysis in Multivariate.py was the moment it clicked. A PairGrid showing KDE contours, scatter overlays, and histograms across every variable combination in one figure — that's the kind of visualization that actually reveals patterns in data.

Built in  Nepal. Part of a self-directed journey into ML and data science.
