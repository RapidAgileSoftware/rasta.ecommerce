import argparse
import logging
import os
import sys

__version__= "0.0.1"


def add_default_args(parser):
    """Add the default options and arguments to the CLI parser.
    Args:
        parser (argparse.ArgumentParser): CLI parser object
    """

    parser.add_argument(
        dest="project",
        help="Your projects name",
        metavar="PROJECT")
    parser.add_argument(
        "--domain",
        "-u",
        dest="domain",
        required=False,
        help="Enter the domain url of your project"
    )
    parser.add_argument(
        "-p",
        "--package",
        dest="package",
        required=False,
        help="github package name (default: project name)",
        metavar="NAME")
    parser.add_argument(
        "-d",
        "--description",
        dest="description",
        required=False,
        help="Describe your project",
        metavar="TEXT")
    parser.add_argument(
        '--version',
        action='version',
        version='Rasta Ecommerce {ver}'.format(ver=__version__))
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        const=logging.INFO,
        dest="log_level",
        help="show additional information about current actions")
    parser.add_argument(
        "-vv",
        "--very-verbose",
        action="store_const",
        const=logging.DEBUG,
        dest="log_level",
        help="show all available information about current actions")


def parse_args(args):
    """Parse command line parameters respecting extensions
    Args:
        args ([str]): command line parameters as list of strings
    Returns:
        dict: command line parameters
    """
    # create the argument parser
    parser = argparse.ArgumentParser(
        description="Let's do some Ecommerce")

    add_default_args(parser)
    # Parse options and transform argparse Namespace object into common dict
    opts = vars(parser.parse_args(args))
    return opts


def process_opts(opts):
    """Process and enrich command line arguments
    Args:
        opts (dict): dictionary of parameters
    Returns:
        dict: dictionary of parameters from command line arguments
    """
    # Remove options with None values
    opts = {k: v for k, v in opts.items() if v is not None}
    return opts


def main(args):
    """Main entry point for external applications
    """
    opts = parse_args(args)
    opts = process_opts(opts)
    print(opts)


def run():
    """Entry point for console script"""
    main(sys.argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
