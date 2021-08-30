import pandas as pd
from GeneralSettings import GeneralSettings as Settings


class ReadData:
    df: pd.DataFrame

    def __init__(self) -> None:
        self.df = pd.read_excel(Settings.PATH_FILE_EXCEL)
        # removing the first 2 rows, because they are not needed
        self.df = self.df.drop(labels=[0, 1], axis=0)

    def get_df_list(self) -> list[pd.DataFrame]:
        number_of_columns = len(self.df.columns)
        split_dfs: list[pd.DataFrame] = []
        for i in range(0, number_of_columns, 2):
            split_dfs.append(self.df.iloc[:, [i, i+1]])
        split_dfs = [df.dropna() for df in split_dfs]
        return split_dfs

