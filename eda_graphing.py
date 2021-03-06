### EDA
#=====================================================================================================
from scipy import stats
stats.mode(a)

# correlation matrix
df.corr() # method='pearson' / 'spearman' / 'kendall'
# covariance matrix
df.cov()
# displays all descriptive statistics
df.describe()
# displays all unique values in 1 column and counts them
df['col'].value_counts()
# displays all unique values in 1 column
df['col'].unique()

x = [1,2,3,4,5]
# returns the mean of the array
np.mean(x)
# returns the median of the array
np.median(x)
# returns the sum of the array
np.sum(x)
# returns the size/shape of the array
np.size(x)
# returns the variance of the array
np.var(x)
# returns the standard deviation of the array
np.std(x)
# returns the square root of the array
np.sqrt(x)
# returns the count occurance of the array 
.count(x)

## Groupby
new_df = df.groupby(['col1'])[['col2', 'col3']].mean().reset_index()
new_df.sort_values('col2', axis=1)
# Groupby col1 with the mean values of col2 and col3, reset the index and sorted by col2
# Must have .size() .mean() .sum() etc... for groupby to work
#=====================================================================================================



#=====================================================================================================
### Colors

# color mapping gradients
cmap_all = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r',
            'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 
            'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 
            'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 
            'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 
            'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 
            'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 
            'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 
            'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cool', 'cool_r', 'coolwarm', 
            'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 
            'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 
            'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot',
            'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 
            'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 
            'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r',
            'spectral', 'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'terrain', 'terrain_r', 'viridis', 
            'viridis_r', 'winter', 'winter_r']
# gradients that have 'white' in the middle (good for heatmaps)
cmap_scales = ['BrBG_r','BrBG','RdGy_r','RdGy','PRGn','PRGn_r','PiYG','PiYG_r','PuOr',
               'PuOr_r','RdBu','RdBu_r','RdGy','RdGy_r','bwr','bwr_r','seismic','seismic_r']
# gradients that are good for kde plots
cmap_gradients = [x for x in cmap_all if x not in cmap_scales]
#=====================================================================================================



### Graphing
#=====================================================================================================
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

# Plot within the jupyter notebook
%matplotlib inline
# Basically, the HD version
%config InlineBackend.figure_format = 'retina'

# Create a figure size
fig = plt.figure(figsize=(7,7))
ax = fig.gca()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Scatterplot
# Seaborn
ax = sns.regplot(x=x, y=y, data=df, color='green', marker='+', ci=68, x_estimater=x, y_jitters=0.1, 
                 x_bins=5, truncate=True, logistic=False)
# Matplotlib
ax.scatter(x, y, s=150, c='blue', label='accepted')
ax.scatter(x, y, s=100, c='orange', label='rejected')

ax.set_ylabel('y label', fontsize=16)
ax.set_xlabel('x label', fontsize=16)
ax.set_title('I am title', fontsize=20)

ax.set_xlim([2.,5.])
ax.set_ylim([-0.1, 1.1])

plt.legend(loc='upper left')
plt.show()

# Add labels to plots
for label, x, y in zip(labels, x, y):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'orange', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    
plt.show()
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Histogram
# Seaborn
ax = sns.distplot(x, name='x variable', fit=norm, kde=False, vertical=False, color='yellow')
# Matplotlib
ax.hist(x, bin=5, alpha=0.7) # Hist for 2 datasets, input [x,y]
ax.set_ylabel('frequency', fontsize=16)
ax.set_xlabel('something', fontsize=16)
ax.set_title('I am title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Lineplot
# Seaborn
ax = sns.pointplot(x=x, y=y, hue='gender',data=df, marker=['o','x'], linestyle=['-','--'], join=True, 
                   color='#bb3f3f', order=['Dinner','Lunch'], estimator=np.median, capsize=.2)
# Matplotlib
ax = sns.plot(x,y)
ax.set_ylabel('y', fontsize=16)
ax.set_xlabel('x', fontsize=16)
ax.set_title('title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Heatmap (Correlate)
# Seaborn
mean_corr = bcw_mean[[x for x in bcw_mean.columns if x not in 'id']].corr()

# Set the default matplotlib figure size:
plt.rcParams['figure.figsize']=(9,7)

# Generate a mask for the upper triangle (taken from seaborn example gallery)
mask = np.zeros_like(mean_corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Plot the heatmap with seaborn.
# Assign the matplotlib axis the function returns. This will let us resize the labels.
ax = sns.heatmap(mean_corr, mask=mask)
# Matplotlib
## It's difficult, use seaborn pls

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Barplot
# Seaborn
ax = sns.barplot(x=x, y=y, data=df, hue='gender', order=['Dinner', 'Lunch'], estimator=np.median, color='b')
# Matplotlib
ax.bar(x, y, width=1.5, color='blue')
ax.set_ylabel('y', fontsize=16)
ax.set_xlabel('x', fontsize=16)
ax.set_title('title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Pairplot
# Seaborn
ax = sns.pairplot(df, hue='gender', markers=['x','o'], size=3, vars=['Height', 'Weight'], kind='reg')

# Create customizable Pairplot
grid = sns.PairGrid(subjective)
grid = grid.map_lower(sns.regplot)
grid = grid.map_diag(plt.hist)
grid = grid.map_upper(sns.kdeplot, cmap='Blues', shade=True, shade_lowest=False)

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Boxplot
# Seaborn
ax = sns.boxplot(x=x, y=y, data=df, hue='gender', orient='h', fliersize=2)
ax = sns.swarmplot(x=x, y=y, data=df, color='.25')
# Another variation
sns.boxplot(x=x, data=rv_df, color='limegreen')
sns.swarmplot(x=x, data=rv_df, color='orange', linewidth=.3)
plt.show()
# Matplotlib
ax.barplot(data)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


## Hexagon Plot
from scipy.stats import kendalltau
sns.set(style="ticks")

# fig = plt.figure(figsize=(12,10))
# ax = fig.gca()

x = rv_df.median_rv_price
y = rv_df.mean_rv_price

sns.jointplot(x, y, kind="hex", stat_func=kendalltau, color="#4CB391 ")
plt.show()
#=====================================================================================================






