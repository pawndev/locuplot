from datetime import datetime

import pandas as pd


class FailuresStats:
    def __init__(self, failures_filepath: str):
        self.df = pd.read_csv(failures_filepath, sep=",")
        self.tasks_name = self.df.Name.unique()

    def get_failures_list(self):
        failures = {}
        for task in self.tasks_name:
            task_df = self.df[self.df.Name == task]
            errors_list = task_df.Error.unique()
            errors = [
                {
                    "name": error,
                    "occurrences": task_df[task_df.Error == error].Occurrences.iloc[0]
                } for error in errors_list
            ]
            failures[task] = errors
        return failures
