import pandas as pd
from .history_stats import HistoryStats
from .failures import FailuresStats


class Stats:
    def __init__(self, history_filepath: str, stats_filepath, failures_filepath):
        self.history = HistoryStats(history_filepath)
        self.generic = pd.read_csv(stats_filepath, sep=",")
        self.failures = FailuresStats(failures_filepath)

