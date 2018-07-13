import logging
import argparse


def logger_from_cli_params(name=__name__):
    parser = argparse.ArgumentParser(description='Liquidated organizations updater for VTiger')
    parser.add_argument("-l", "--log", dest="loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level", default='WARNING')
    args = parser.parse_args()
    loglevel = getattr(logging, args.loglevel, None)
    logging.basicConfig(level=loglevel)
    return logging.getLogger(name)
