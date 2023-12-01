import logging
logger = logging.getLogger( __name__ )

class Trebuchet:

    def __init__( self, coordinate_list ):

        self.coordinate_list = coordinate_list
        
    # ------- 
    def get_coordinates( self ):
        for coordinate in self._get_coordinates():
            print( self.get_integers( coordinate ) )

    def get_integers( self, coordinate ):
        int_list = []

        for x in coordinate:
            print (x)
            if x.isdigit():
                int_list.append( x )

        return int_list

    def _get_coordinates( self ):
        for coordinate in self.coordinate_list:
            yield coordinate
