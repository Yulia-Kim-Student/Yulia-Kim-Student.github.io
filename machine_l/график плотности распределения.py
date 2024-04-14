import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Union

def draw_pdf(data: pd.DataFrame, column: str, bins: Union[int, str] = 10) -> None:

    bin_edges = np.histogram_bin_edges(data[column], bins=bins)

    hist = data[column].plot(kind='hist', bins=bin_edges, density=True, color='orange', edgecolor='black')
    data[column].plot(kind='kde', ax=hist, color='black', linewidth=3)

    hist.set_xlim(data[column].min(), data[column].max())
    hist.set_ylabel('')
    hist.set_xlabel(column)
    hist.legend(['Density', 'KDE'])
    plt.grid(True)


data = pd.read_csv('plotnost_rasp.csv')
plt.figure(figsize=(10, 5))
plt.rcParams.update({'font.size': 14})
draw_pdf(data, 'Account length', 'sturges')
plt.savefig('output.png')