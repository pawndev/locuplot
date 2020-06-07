import os
from logzero import logger
from .argument_parser import parse_args, validate_args, format_args
from .locust.stats import Stats
from .helpers.fs import create_dir
from .helpers.plot import save_plot
import matplotlib.pyplot as plt
import mpld3
import jinja2


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
    failures = stats.failures.get_failures_list()
    d3_graph =[]
    history_figures = stats.history.generate_all_plot()
    percentiles = stats.history.generate_all_percentile_tables()
    for history_task in history_figures:
        # mpld3.save_html(history_task.get('req_per_sec_figure'), os.path.join(formatted_args.export_dir, 'req_per_second', '{}.html'.format(history_task.get('name'))))
        # mpld3.save_html(history_task.get('response_times_figure'), os.path.join(formatted_args.export_dir, 'response_times', '{}.html'.format(history_task.get('name'))))
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
    data = {
        "history_figures": history_figures,
        "percentiles": percentiles,
        "failures": failures
    }
    main_dir = os.path.dirname(os.path.realpath(__file__))
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.join(main_dir, 'templates'))
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "template.html"
    template = template_env.get_template(template_file)
    output_html = template.render(data=data)
    with open(os.path.join(formatted_args.export_dir, 'index.html'), 'w', encoding='utf-8') as outfile:
        outfile.write(output_html)
    logger.info('All done!')
