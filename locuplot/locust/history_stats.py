from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


class HistoryStats:
    def __init__(self, history_filepath: str):
        self.df = pd.read_csv(history_filepath, sep=",")
        self.df["datetime"] = self.df["Timestamp"].apply(lambda t: datetime.fromtimestamp(t))

    def generate_history_plot(self):
        ax1 = plt.gca()
        self.df.plot(x="datetime", y="Requests/s", ax=ax1)
        self.df.plot(x="datetime", y="Failures/s", ax=ax1)
        fig = plt.gcf()
        return fig
