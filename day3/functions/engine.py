import logging
logger = logging.getLogger( __name__ )

from functions.part import Part

class Engine:

    def __init__( self ):
        self.part_list = []

    # -------
    def add_part( self, part_data ):
        self.part_list.append( Part( part_data ) )

    def print_parts( self ):
        for part in self.part_list:
            print( part.print_components() )