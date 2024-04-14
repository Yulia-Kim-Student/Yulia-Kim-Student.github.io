import pandas as pd

def fillna_date(data: pd.DataFrame, function: str = 'mean') -> pd.DataFrame:

    data.index = pd.to_datetime(data.index)
    filled_m = data.fillna(data.resample('M').transform(function))
    filled_y = filled_m.fillna(filled_m.resample('Y').transform(function))
    filled_full = filled_y.fillna(getattr(filled_y, function)())
    return filled_full


data = pd.read_csv('fillna.csv', index_col='date')
data = fillna_date(data)
data.to_csv('output.csv')
# a = pd.read_csv('output.csv')
# b = pd.read_csv('output (2).csv')
# c = a == b
# c.index = a['date']
# c.to_csv('test.csv')

