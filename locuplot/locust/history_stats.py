from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


class HistoryStats:
    def __init__(self, history_filepath: str):
        self.df = pd.read_csv(history_filepath, sep=",")
        self.df["datetime"] = self.df["Timestamp"].apply(lambda t: datetime.fromtimestamp(t))

    def generate_response_times_plot(self, df):
        plt.figure()
        ax = plt.gca()
        df.plot(x="datetime", y="Total Median Response Time", ax=ax)
        df.plot(x="datetime", y="95%", ax=ax)
        df.plot(x="datetime", y="75%", ax=ax)
        df.plot(x="datetime", y="50%", ax=ax)
        fig = plt.gcf()
        return fig

    def generate_req_per_sec_plot(self, df):
        plt.figure()
        ax = plt.gca()
        df.plot(x="datetime", y="Requests/s", ax=ax, color="blue")
        df.plot(x="datetime", y="Failures/s", ax=ax, color="red")
        fig = plt.gcf()
        return fig

    def generate_all_req_per_sec_plot(self):
        """
        Generate all figures
        :return: Array<{name: string, figure: Figure}>
        """
        tasks_name = self.df.Name.unique()
        return [
            {
                "name": task,
                "req_per_sec_figure": self.generate_req_per_sec_plot(self.df[self.df.Name == task]),
                "response_times_figure": self.generate_response_times_plot(self.df[self.df.Name == task])
            } for task in tasks_name
        ]

