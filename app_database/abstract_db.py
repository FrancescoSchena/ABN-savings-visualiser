from enum import Enum

import pandas as pd


class WriteMode(Enum):
    OVERWRITE = "overwrite"
    APPEND = "append"


class Table(Enum):
    TRANSACTIONS = "transactions"


class DataBase:
    def __init__(self):
        pass

    def read_from_table(self, table: Table) -> pd.DataFrame:
        pass

    def write_to_table(self, table: Table, write_mode: WriteMode) -> None:
        pass
