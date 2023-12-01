import logging
logger = logging.getLogger( __name__ )

class Trebuchet:

    def __init__( self, coordinate_list ):

        self.coordinate_list = coordinate_list
        self.coordinate_generator = None
        self.coordinate_sum_running_total = 0

    # -------
    def get_coordinates( self ):
        self.set_coordinates_generator()
        self.get_integers()

    def get_integers( self ):
        for coordinate in self.coordinate_generator:
            self.coordinate_sum_running_total += self._get_first_last_int( self._get_integers( coordinate ) )

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

    def _get_first_last_int( self, int_list ):
        return int( int_list[0] + int_list[-1] )
