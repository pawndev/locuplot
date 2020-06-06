import os
from .argument_parser import parse_args, validate_args, format_args
from .locust.stats import Stats
from .helpers.fs import create_dir
from .helpers.plot import save_plot


def main():
    args = parse_args()
    validate_args(args)
    formatted_args = format_args(args)
    create_dir(formatted_args.export_dir)
    create_dir(os.path.join(formatted_args.export_dir, 'req_per_second'))
    create_dir(os.path.join(formatted_args.export_dir, 'response_times'))
    stats = Stats(
        history_filepath=formatted_args.history_filepath,
        stats_filepath=formatted_args.stats_filepath,
        failures_filepath=formatted_args.failures_filepath
    )
    history_figures = stats.history.generate_all_req_per_sec_plot()
    for history_task in history_figures:
        save_plot(
            history_task.get('req_per_sec_figure'),
            os.path.join(formatted_args.export_dir, 'req_per_second'),
            '{}.png'.format(history_task.get('name')),
            'png'
        )
        save_plot(
            history_task.get('response_times_figure'),
            os.path.join(formatted_args.export_dir, 'response_times'),
            '{}.png'.format(history_task.get('name')),
            'png'
        )
