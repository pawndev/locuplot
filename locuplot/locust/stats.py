import pandas as pd
from .history_stats import HistoryStats
from .failures import FailuresStats
from .generic import GenericStats


class Stats:
    def __init__(self, history_filepath: str, stats_filepath, failures_filepath):
        self.history = HistoryStats(history_filepath)
        self.generic = GenericStats(stats_filepath)
        self.failures = FailuresStats(failures_filepath)

