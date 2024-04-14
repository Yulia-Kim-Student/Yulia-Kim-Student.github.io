import pandas as pd

def get_businessmen(df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает DataFrame, оставляя в нём только пользователей из df,
    совершивших 20 и более международных звонков

    Параметры:
      df: исходный DataFrame

    Возвращаемое значение:
      отфильтрованный DataFrame
    """
    mask = df['Total intl calls'] >= 20
    result_df = df.loc[mask]
    return result_df
