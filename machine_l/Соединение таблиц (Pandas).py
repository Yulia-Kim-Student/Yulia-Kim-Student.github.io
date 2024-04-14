import pandas as pd

State = pd.read_csv('Штаты.csv', index_col='ID')
User = pd.read_csv('Пользователи.csv', index_col='ID')
def join_dataframes(users_df: pd.DataFrame, states_df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает объединённый DataFrame

    Параметры:
      users_df: DataFrame с пользователями - столбцы: 'ID', 'State ID', 'Total day calls', 'Total night calls'
      states_df: DataFrame с штатами - столбцы: 'ID', 'State'

    Возвращаемое значение:
      объединённый DataFrame, содержащий поля 'Total day calls', 'Total night calls', 'State' в данном порядке
    """
    joined_df = pd.merge(users_df, states_df, how='left', left_on='State ID', right_on='ID')
    joined_df = joined_df[['Total day calls', 'Total night calls', 'State']]
    return joined_df.set_index(users_df.index)

print(join_dataframes(User, State))
# print(User)
# print(State)