from .argument_parser import parse_args, validate_args, format_args
from .locust.stats import Stats
from .helpers.fs import create_dir
from .helpers.plot import save_plot

def main():
    args = parse_args()
    validate_args(args)
    formatted_args = format_args(args)
    create_dir(formatted_args.export_dir)
    stats = Stats(
        history_filepath=formatted_args.history_filepath,
        stats_filepath=formatted_args.stats_filepath,
        failures_filepath=formatted_args.failures_filepath
    )
    history_figure = stats.history.generate_history_plot()
    save_plot(history_figure, formatted_args.export_dir, 'global_req_per_second.png', 'png')

