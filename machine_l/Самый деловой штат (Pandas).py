import pandas as pd
data = pd.read_csv('Самый деловой штат.csv')
print(data)

def get_busiest_states(data: pd.DataFrame) -> pd.Series:
    """
    Вычисляет Series, в котором индексы - наименования штатов, а значение - количество совершённых международных звонов.

    Параметры:
      data: DataFrame с данными

    Возвращаемое значение:
      Series отсортированный по убыванию значений.
    """
    series = data.groupby('State')['Total intl calls'].sum().sort_values(ascending=False)
    return series

print(get_busiest_states(data))
print(type(get_busiest_states(data)))
