import logging
logger = logging.getLogger( __name__ )

class CubeGameController:

    def __init__( self, game_data_input ):

        self.game_data_input = ( game_data_input.replace( " ", "" ) ).replace( "\n", "" )

        self.game_data = self.game_data_input.split( ':' )[0]
        self.set_data = self.game_data_input.split( ':' )[1]

        self.game_data = self.game_data.split( 'Game' )[1]

    # -------
    def get_sets( self ):
        return self._get_sets()

    def get_game( self ):
        return self._get_game()

    # -------
    def _get_sets( self ):
        return self.set_data.split(';')

    def _get_game( self ):
        return self.game_data