import os.path

import argparse
import logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level = logging.INFO )

# -------
class AOC_App( object ):

    def __init__( self ):
        pass

    # -------
    def run( self ):
        try:
            self.execute(  )
            return True

        except Exception as ex:
            logger.exception( ex )
            return False

    def execute( self ):
        pass

    def get_file_contents( self, file_path ):
        pass

    # -------
    def parse_args( self, args):

        parser = argparse.ArgumentParser(
            description = "AOC 2023" )
        parser.add_argument( "--xx-x",
            dest = "xxx",
            help = "xxxx")

        args = parser.parse_args( args )
        self.xxx = args.xxx

    # -------
    def validate_args( self ):
        assert self.xxx, "xxx"
