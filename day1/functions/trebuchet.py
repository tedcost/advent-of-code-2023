import logging
logger = logging.getLogger( __name__ )

class Trebuchet:

    def __init__( self, coordinate_list ):

        self.coordinate_list = coordinate_list
        self.coordinate_generator = None
        self.calibration_value_running_total = 0
        self.calibration_string_value_running_total = 0
        self.string_int_dict = [
            { 'string':'nine', 'int': 'n9e' },
            { 'string':'eight', 'int': 'e8t' },
            { 'string':'seven', 'int': 's7n' },
            { 'string':'six', 'int': 's6x' },
            { 'string':'five', 'int': 'f5e' },
            { 'string':'four', 'int': 'f4r' },
            { 'string':'three', 'int': 't3e' },
            { 'string':'two', 'int': 't2o' },
            { 'string':'one', 'int': 'o1e' }
        ]

    # -------
    def set_calibration_value( self ):
        self.set_coordinates_generator()
        self.get_integers()

    def set_coordinates_generator( self ):
        self.coordinate_generator = self._get_coordinates_generator()

    def get_integers( self ):
        integers_list = []
        string_integers_list = []

        for coordinate in self.coordinate_generator:
            integers_list = self._get_integers( coordinate )
            self.calibration_value_running_total += self._get_first_last_int( integers_list )

            string_integers_list = self._get_integers( self._replace_string_ints( coordinate ) )
            self.calibration_string_value_running_total += self._get_first_last_int( string_integers_list )

            print(coordinate)
            print(integers_list)
            print(self.calibration_value_running_total)
            print(string_integers_list)
            print(self.calibration_string_value_running_total)
            print('\n')

    def get_calibration_value( self ):
        return self._get_calibration_value()

    def get_calibration_string_value( self ):
        return self._get_calibration_string_value()



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

    def _replace_string_ints( self, coordinate ):
        for i in self.string_int_dict:
            if i['string'] in coordinate:
                coordinate = coordinate.replace( i['string'], i['int'] )

        return coordinate

    def _get_first_last_int( self, int_list ):
        return int( int_list[0] + int_list[-1] )

    def _get_calibration_value( self ):
        return self.calibration_value_running_total

    def _get_calibration_string_value( self ):
        return self.calibration_string_value_running_total
