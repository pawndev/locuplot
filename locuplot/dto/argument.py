from os import path

class Argument:
    def __init__(self, directory: str, prefix: str, export_dir: str):
        self.dir = directory
        self.prefix = prefix
        self.export_dir = export_dir
        self.history_filepath = path.join(directory, "{}_stats_history.csv".format(prefix))
        self.stats_filepath = path.join(directory, "{}_stats.csv".format(prefix))
        self.failures_filepath = path.join(directory, "{}_failures.csv".format(prefix))
