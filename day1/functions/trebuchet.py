import logging
logger = logging.getLogger( __name__ )

class Trebuchet:

    def __init__( self, coordinate_list ):

        self.coordinate_list = coordinate_list
        self.coordinate_generator = None

    # -------
    def get_coordinates( self ):
        self.set_coordinates_generator()
        self.get_integers()

    def get_integers( self ):
        for coordinate in self.coordinate_generator:
            print ( self._get_integers( coordinate ) )

    def set_coordinates_generator( self ):
        self.coordinate_generator = self._get_coordinates_generator()


    # -------
    def _get_coordinates_generator( self ):
        for coordinate in self.coordinate_list:
            yield coordinate

    def _get_integers( self, coordinate ):
        int_list = []

        for x in coordinate:
            if x.isdigit():
                int_list.append( x )

        return int_list
