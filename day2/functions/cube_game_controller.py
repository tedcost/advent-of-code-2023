import logging
logger = logging.getLogger( __name__ )

from functions.set import Set

class CubeGameController:

    def __init__( self, game_data_input ):

        self.game_data_input = ( game_data_input.replace( " ", "" ) ).replace( "\n", "" )

        self.game_data = self.game_data_input.split( ':' )[0]
        self.set_data = self.game_data_input.split( ':' )[1]

        self.game_data = self.game_data.split( 'Game' )[1]
        self.set_list = []

        self.blue_max = 0
        self.red_max = 0
        self.green_max = 0

    # -------
    def get_sets( self ):
        return self._get_sets()

    def get_game( self ):
        return self._get_game()

    def load_sets( self ):
        for game_set in self.get_sets():
            self.set_list.append( Set( game_set ) )

    def print_sets( self ):
        for game_set in self.set_list:
            print('Blue: %s' % game_set.get_blue_count() )
            print('Red: %s' % game_set.get_red_count() )
            print('Green: %s' % game_set.get_green_count() )

    def print_max_colors( self ):
        print('Blue: %s' % self.blue_max )
        print('Red: %s' % self.red_max )
        print('Green: %s' % self.green_max )

    def set_max_colors( self ):
        for game_set in self.set_list:
            if game_set.get_blue_count() > self.blue_max:
                self.blue_max = game_set.get_blue_count()
            if game_set.get_red_count() > self.red_max:
                self.red_max = game_set.get_red_count()
            if game_set.get_green_count() > self.green_max:
                self.green_max = game_set.get_green_count()

    # -------
    def _get_sets( self ):
        return self.set_data.split(';')

    def _get_game( self ):
        return int( self.game_data )
