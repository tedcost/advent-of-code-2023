import os.path

import argparse
import logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level = logging.INFO )

from functions.get_file_contents import GetFileContents
from functions.cube_game_controller import CubeGameController

# -------
class AOC_App( object ):

    def __init__( self ):
        self.input_file = None
        self.blue_cube_count = 0
        self.red_cube_count = 0
        self.green_cube_count = 0

        self.acceptable_game_count = 0
        self.game_power_count = 0

    # -------
    def run( self ):
        try:
            file_contents_list = self.get_file_contents( self.input_file )
            self.execute( file_contents_list )
            return True

        except Exception as ex:
            logger.exception( ex )
            return False

    def execute( self, file_contents_list ):
        for game in file_contents_list:
            cube_controller = CubeGameController( game )
            cube_controller.load_sets()
            cube_controller.set_max_colors()

            print( cube_controller.get_sets() )
            print( cube_controller.get_game() )
            
            #cube_controller.print_sets()
            #cube_controller.print_max_colors()

            if cube_controller.blue_max <= self.blue_cube_count and \
                cube_controller.red_max <= self.red_cube_count and \
                cube_controller.green_max <= self.green_cube_count:
                    self.acceptable_game_count += cube_controller.get_game()

            print( self.acceptable_game_count )
            print( cube_controller.get_game_power() )
            self.game_power_count += cube_controller.get_game_power()

        print( self.game_power_count )

    def get_file_contents( self, file_path ):
        file_contents_obj = GetFileContents( file_path )
        return file_contents_obj.read_file()

    # -------
    def parse_args( self, args):

        parser = argparse.ArgumentParser(
            description = "AOC 2023" )
        parser.add_argument( "--input-file",
            dest = "input_file",
            help = "Input file for the given AOC challenge")
        parser.add_argument( "--blue-cube-count",
            dest = "blue_cube_count",
            help = "The amount of blue cubes we are comparing each game against!")
        parser.add_argument( "--red-cube-count",
            dest = "red_cube_count",
            help = "The amount of red cubes we are comparing each game against!")
        parser.add_argument( "--green-cube-count",
            dest = "green_cube_count",
            help = "The amount of green cubes we are comparing each game against!")

        args = parser.parse_args( args )
        self.input_file = args.input_file
        self.blue_cube_count = args.blue_cube_count
        self.red_cube_count = args.red_cube_count
        self.green_cube_count = args.green_cube_count

    # -------
    def validate_args( self ):
        assert self.input_file, "Input file required for app to function."
        assert self.blue_cube_count, "Blue Cube Count required for app to function."
        assert self.red_cube_count, "Red Cube Count required for app to function."
        assert self.green_cube_count, "Green Cube Count required for app to function."

        assert self.input_file[-4:] == ".txt", "Input file is not a .txt file. Input file must be .txt."
        assert os.path.exists( self.input_file ), "Data File does not exist."

        assert self.blue_cube_count.isdigit(), "Cube count must be an integer!"
        assert self.red_cube_count.isdigit(), "Cube count must be an integer!"
        assert self.green_cube_count.isdigit(), "Cube count must be an integer!"

        self.blue_cube_count = int( self.blue_cube_count )
        self.red_cube_count = int( self.red_cube_count )
        self.green_cube_count = int( self.green_cube_count )
