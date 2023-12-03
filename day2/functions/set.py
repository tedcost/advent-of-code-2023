import logging
logger = logging.getLogger( __name__ )

class Set:

    def __init__( self, set_data ):
        self.set_data = set_data
        self.blue_count = 0
        self.red_count = 0
        self.green_count = 0

        self.parse_set_data()

    # -------
    def parse_set_data( self ):
        set_data_list = self.set_data.split( ',' )
        for game_set in set_data_list:
            if 'blue' in game_set:
                self.blue_count = game_set.split( 'blue' )[0]
            if 'red' in game_set:
                self.red_count = game_set.split( 'red' )[0]
            if 'green' in game_set:
                self.green_count = game_set.split( 'green' )[0]

    def get_blue_count( self ):
        return int( self.blue_count )
    def get_red_count( self ):
        return int( self.red_count )
    def get_green_count( self ):
        return int( self.green_count )
