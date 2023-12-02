import os.path

import argparse
import logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level = logging.INFO )

from functions.get_file_contents import GetFileContents
from functions.trebuchet import Trebuchet

# -------
class AOC_App( object ):

    def __init__( self ):
        self.input_file = None

    # -------
    def run( self ):
        try:
            file_contents_list = self.get_file_contents( self.input_file )
            self.execute( file_contents_list )
            return True

        except Exception as ex:
            logger.exception( ex )
            return False

    def execute( self, file_contents_list ):
        trebuchet_obj = Trebuchet( file_contents_list )
        trebuchet_obj.set_calibration_value()
        print( trebuchet_obj.get_calibration_value() )
        print( trebuchet_obj.get_calibration_string_value() )

    def get_file_contents( self, file_path ):
        file_contents_obj = GetFileContents( file_path )
        return file_contents_obj.read_file()

    # -------
    def parse_args( self, args):

        parser = argparse.ArgumentParser(
            description = "AOC 2023" )
        parser.add_argument( "--input-file",
            dest = "input_file",
            help = "Input file for the given AOC challenge")

        args = parser.parse_args( args )
        self.input_file = args.input_file

    # -------
    def validate_args( self ):
        assert self.input_file, "Input file required for app to function."
        assert self.input_file[-4:] == ".txt", "Input file is not a .txt file. Input file must be .txt."
        assert os.path.exists( self.input_file ), "Data File does not exist."
