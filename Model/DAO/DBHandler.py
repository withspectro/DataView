import os
import sqlite3
import pandas as pd


class DBHandler():
    def __init__(self):
        self.__parent_path = os.getcwd() + '\\'
        self.__db_file_name = 'jinji.db'

    def connect_db(self):
        con = sqlite3.connect(self.__db_file_name)
        return con

    def update_data_table(self, DataFrame: pd.DataFrame, table_name:str):
        con = self.connect_db()
        DataFrame.to_sql(table_name, con, if_exists='append')
        con.close()

    def read_data_table(self, table_name:str, start_date:str, end_date:str):
        con = self.connect_db()
        df = pd.read_sql("SELECT * FROM [{name}] WHERE time_axis >= '{start}' AND time_axis <= '{end}' ".format(name=table_name, start=start_date, end=end_date), con=con)
        con.close()
        return df
