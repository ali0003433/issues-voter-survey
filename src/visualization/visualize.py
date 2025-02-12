import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_bar(x, y, palette, title, xlabels): 
    '''
    Create seaborn bar plot  

    Args:
        x ()
        y ()
        palette (list)
        title (string)    
        xlabels (list)
    Returns:
        plot object  
    '''
    plt.figure(figsize=(10, 5))
    bar_plot = sns.barplot(x=x, y=y,palette=palette)
    bar_plot.set_title(title)
    bar_plot.set_xticklabels(rotation=90, labels=xlabels)
    bar_plot.set_ylabel('Weighted frequency')
    bar_plot.set(ylim=(0, .5))
    return bar_plot


def plot_stacked(data, title):
    '''
    Create stacked bar plot  

    Args:
        data ()
        title (string)
    Returns:
        plot object  
    '''
    palette_short = ['cornflowerblue','tomato','lightgrey']
    stacked_plot = data.T.plot(kind='bar', stacked=True, color=palette_short)
    stacked_plot.set_title(title)
    pres_cat_list = ['Clinton', 'Trump', 'Other behavior']
    stacked_plot.legend(pres_cat_list)
    N = 5 
    ind = np.arange(N)
    stacked_plot.set_xlabel('')
    x_ticks = ('Very','Somewhat','Not very', 'Unimportant', 'No Response')
    y_label = 'Weighted frequency'
    plt.xticks(ind, x_ticks)
    stacked_plot.set_ylabel(y_label)
    stacked_plot.set(ylim=(0,2.1))
    return stacked_plot

def count_res(df):
    '''
    Count each category of resonse and return dictionary 

    Args:
        df (dataframe)
    Returns:
        dictionary of response counts 
    '''
    count_dict = {1: 0, 2: 0, 3: 0, 4: 0, 8: 0}
    for idx, row in df.iterrows():
        for col in df.columns:
            res = row[col]
            count_dict[res] +=1
    return count_dict