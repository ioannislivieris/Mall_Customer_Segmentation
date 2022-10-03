# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Built-in libraries
#
import pandas as pd


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Visualization libraries
#
import matplotlib.pyplot as plt
import seaborn           as sns





def snake_plot(df, labels, CustomerIDs):

    df['Cluster']    = labels
    df['CustomerID'] = CustomerIDs
    

    # Melt data into long format
    df_melt = pd.melt(df.reset_index(), 
                      id_vars    = ['CustomerID', 'Cluster'],
                      value_vars = ['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'], 
                      var_name   = 'Metric', 
                      value_name = 'Value')

    plt.figure( figsize = (15, 4) )
    sns.pointplot(data = df_melt, x = 'Metric', y = 'Value', hue = 'Cluster')

    plt.xlabel('Metric', size = 14)
    plt.ylabel('Value',  size = 14)
    plt.xticks(size = 12)
    plt.xticks(size = 12)
    plt.legend(frameon = True, fontsize = 12)
    plt.show()
    