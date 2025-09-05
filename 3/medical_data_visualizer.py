
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("./medical_examination.csv")

# 2

imc = df['weight'] / (df['height'] / 100) ** 2
df.loc[imc > 25, "overweight"] = 1
df.loc[imc < 25, "overweight"] = 0

print(df['overweight'].value_counts())


# 3
normalizados = ['gluc', 'cholesterol']

for norm in normalizados:
    df.loc[df[norm] == 1 , norm] = 0
    df.loc[df[norm] > 1 , norm] = 1

    print(df[norm].value_counts())

# 4
def draw_cat_plot():
    # 6
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    # 7
    df_cat = df_cat.groupby(['cardio', 'n', 'valor']).size().reset_index(name='total')

    # 8
    fig = sns.catplot(x='n', y='total', hue='valor', col='cardio', kind='bar', data=df_cat
    )
    plt.show()
    
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
  # 11️
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  (df['height'] >= df['height'].quantile(0.025)) &  (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))   
    ]

    # 12️
    corr = df_heat.corr()

    # 13️
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14️
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15️
    sns.heatmap(
        corr,mask=mask,annot=True,fmt=".1f",center=0,vmax=0.3,vmin=-0.1,square=True,linewidths=.5,cbar_kws={"shrink": .5},ax=ax
    )

    # 16️
    plt.show()
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()