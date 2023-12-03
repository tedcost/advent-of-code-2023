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

    # -------
    def print_sets( self ):
        return self._print_sets()

    def get_game( self ):
        return self._get_game()

    def load_sets( self ):
        for game_set in self.print_sets():
            self.set_list.append( Set( game_set ) )

    def get_sets( self ):
        for game_set in self.set_list:
            print('Blue: %s' %  game_set.get_blue_count() )
            print('Red: %s' %  game_set.get_blue_count() )
            print('Green: %s' %  game_set.get_blue_count() )

    # -------
    def _print_sets( self ):
        return self.set_data.split(';')

    def _get_game( self ):
        return self.game_data