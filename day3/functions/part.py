import re

import logging
logger = logging.getLogger( __name__ )

class Part:

    def __init__( self, part_data ):
        self.part_data = part_data
        self.component_list = []

        self.add_component()

    # -------
    def print_components( self ):
        return self.component_list

    def add_component( self ):

        indv_part_list = re.split( '([^a-zA-Z0-9])', self.part_data )
        indv_part_list= [ i for i in indv_part_list if i != '' ]

        for index, item in enumerate( indv_part_list ):
            if item != '.':
                component = {}
                component[ 'position' ] = index
                component[ 'item' ] = item

                self.component_list.append( component)