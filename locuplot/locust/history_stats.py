from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import mpld3


class HistoryStats:
    def __init__(self, history_filepath: str):
        self.df = pd.read_csv(history_filepath, sep=",")
        self.df["datetime"] = self.df["Timestamp"].apply(lambda t: datetime.fromtimestamp(t))
        self.tasks_name = self.df.Name.unique()

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

    def generate_all_plot(self):
        """
        Generate all figures
        :return: Array<{name: string, figure: Figure}>
        """
        plots = []
        for task in self.tasks_name:
            req_per_sec_figure = self.generate_req_per_sec_plot(self.df[self.df.Name == task])
            response_times_figure = self.generate_response_times_plot(self.df[self.df.Name == task])
            req_per_sec_d3 = mpld3.fig_to_html(req_per_sec_figure)
            response_times_d3 = mpld3.fig_to_html(response_times_figure)

            plots.append({
                "name": task,
                "req_per_sec_figure": req_per_sec_figure,
                "response_times_figure": response_times_figure,
                "req_per_sec_d3": req_per_sec_d3,
                "response_times_d3": response_times_d3
            })
        return plots

    def generate_percentile_table(self, df):
        percentile = df[
            ["Requests/s", "50%", "66%", "75%", "80%", "90%", "95%", "98%", "99%", "99.9%", "99.99%", "99.999%",
             "100%"]].mean()
        return percentile.to_dict()

    def generate_all_percentile_tables(self):
        return [
            {
                "name": task,
                "percentile_table": self.generate_percentile_table(self.df[self.df.Name == task])
            } for task in self.tasks_name
        ]
