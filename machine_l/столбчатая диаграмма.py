import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def draw_bars(data: pd.DataFrame, column: str, target_column: str) -> None:
    group_data = data.groupby(column)[target_column].value_counts(normalize=True).unstack()
    group_data = group_data.sort_index()
    group_data = group_data.fillna(0)
    group_data *= 100
    axis = plt.gca()
    bottom = np.zeros(len(group_data))
    for i in group_data:
        pl = axis.bar(group_data.index, group_data[i], width=0.75, label=i, bottom=bottom)
        bottom += group_data[i].values
        for rect, value in zip(pl, group_data[i].values):
            if value > 5:
                height = rect.get_height()
                label_position = rect.get_y() + height / 2
                axis.text(rect.get_x() + rect.get_width() / 2, label_position, f"{value:.2f} %", ha='center', va='center')
        plt.xticks(range(len(group_data)))
    axis.legend(title=target_column)
    axis.set_xlabel(column)


data = pd.read_csv('столбчатая.csv')

plt.figure(figsize=(10, 5))
plt.rcParams.update({ 'font.size': 8 })

draw_bars(data, 'Customer service calls', 'Total intl calls')
plt.savefig('output.png')

a = plt.get_cmap('tab10')
print(type(a))