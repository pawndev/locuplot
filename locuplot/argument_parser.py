import argparse
import sys
import locuplot
import glob
from logzero import logger
from os import path
from .dto.argument import Argument


def bad_arg(error_message):
    logger.error(error_message)
    sys.exit(128)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    # parser.add_argument("arg", help="Required positional argument")
    parser.add_argument("-d", "--directory", help="Folder where the statistics csv file are.", action="store",
                        default=None)
    parser.add_argument("-p", "--prefix", help="Prefix for locust statistics files", action="store", default=None)
    parser.add_argument("-e", "--export", help="Export directory", action="store", default="dist")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=locuplot.__version__))

    args = parser.parse_args()

    return args


def validate_args(args: argparse.Namespace):
    if args.directory is None:
        bad_arg("Argument directory is missing.")
    if args.prefix is None:
        bad_arg("Argument prefix is missing.")
    if path.exists(args.directory) is False:
        bad_arg("Statistics directory not exist.")
    if not glob.glob("{}_*".format(path.join(args.directory, args.prefix))):
        bad_arg("No file with this prefix was found in this directory.")


def format_args(args: argparse.Namespace):
    return Argument(args.directory, args.prefix, args.export)
