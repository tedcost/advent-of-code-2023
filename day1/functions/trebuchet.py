import logging
logger = logging.getLogger( __name__ )

class Trebuchet:

    def __init__( self, coordinate_list ):

        self.coordinate_list = coordinate_list
        
    # ------- 
    def get_coordinates( self ):
        return _get_coordinates()

    def _get_coordinates( self ):
        for coordinate in self.coordinate_list:
            print( coordinate )
