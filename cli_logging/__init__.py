import logging
import argparse


def logger_from_cli_params(name=__name__):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log", dest="loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level", default='WARNING')
    args, unknown = parser.parse_known_args()
    loglevel = getattr(logging, args.loglevel, None)
    logging.basicConfig(level=loglevel)
    return logging.getLogger(name)
