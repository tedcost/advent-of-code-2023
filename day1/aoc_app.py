import os.path

import argparse
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)

# -------
class AOC_App(object):

    def __init__(self):
        pass
    # -------
    def run(self):
        try:

            return True
        except Exception as ex:
            logger.exception( ex )
            return False

    def execute(self, ):
        pass

    # -------
    def parse_args(self, args):

        parser = argparse.ArgumentParser(
            description = "AOC 2023")
        parser.add_argument( "--input-file",
            dest = "input_file",
            help = "Input file for the given AOC challenge")

        args = parser.parse_args( args )
        self.input_file = args.input_file

    # -------
    def validate_args(self):
        assert self.input_file, "Input file required for app to function."
        assert self.input_file[-4:] == ".txt", "Input file is not a .txt file. Input file must be .txt."
        assert os.path.exists(self.input_file), "Data File does not exist."
