from datetime import datetime

import pandas as pd


class GenericStats:
    def __init__(self, stats_filepath: str):
        self.df = pd.read_csv(stats_filepath, sep=",")

    def get_reporting(self):
        return self.df.to_dict()