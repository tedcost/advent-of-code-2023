import logging
logger = logging.getLogger( __name__ )

from functions.part import Part

class Engine:

    def __init__( self ):
        self.part_list = []
        self.valid_component_count = 0
        self.adjacent_part_counter = 0

    # -------
    def add_part( self, part_data ):
        self.part_list.append( Part( part_data ) )

    def print_parts( self ):
        for part in self.part_list:
            print( part.print_components() )

    def get_entire_number( self, starting_int, list_position, origin_list ):

        if starting_int.isnumeric():
            if origin_list[ list_position + 1 ].isnumeric():
                starting_int = starting_int + origin_list[ list_position + 1 ]

                if origin_list[ list_position + 2 ].isnumeric():
                    starting_int = starting_int + origin_list[ list_position + 2 ]

            if origin_list[ list_position - 1 ].isnumeric():
                starting_int = origin_list[ list_position - 1 ] + starting_int

                if origin_list[ list_position - 2 ].isnumeric():
                    starting_int =  origin_list[ list_position - 2 ] + starting_int

        return starting_int


    def find_valid_components( self ):
        for index_part, part in enumerate( self.part_list ):
            print( part.print_components() )
            for index_comp, component in enumerate ( part.print_components() ):
                if component.isnumeric() == False and component != '.':

                    # Previous Line
                    if ( index_part - 1 ) >= 0:
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part - 1].component_list[ index_comp - 1], index_comp - 1, self.part_list[ index_part - 1].component_list ), end=""  )
                        except:
                            pass
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part - 1].component_list[ index_comp ], index_comp, self.part_list[ index_part - 1].component_list ), end=""  )
                        except:
                            pass
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part - 1].component_list[ index_comp + 1], index_comp + 1, self.part_list[ index_part - 1].component_list ) )
                        except:
                            pass

                    # Current Line
                    try:
                        print ( self.get_entire_number( self.part_list[ index_part ].component_list[ index_comp - 1], index_comp - 1, self.part_list[ index_part ].component_list ), end=""  )
                    except:
                        pass
                    try:
                        print( part.component_list[ index_comp ], end="" )
                    except:
                        pass
                    try:
                        print ( self.get_entire_number( self.part_list[ index_part ].component_list[ index_comp + 1], index_comp + 1, self.part_list[ index_part ].component_list ))
                    except:
                        pass

                    # Future Line
                    if ( index_part + 1 ) <= len( self.part_list ):
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part + 1].component_list[ index_comp - 1], index_comp - 1, self.part_list[ index_part + 1].component_list ), end=""  )
                        except:
                            pass
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part + 1].component_list[ index_comp ], index_comp, self.part_list[ index_part + 1].component_list ), end=""  )
                        except:
                            pass
                        try:
                            print ( self.get_entire_number( self.part_list[ index_part + 1].component_list[ index_comp + 1], index_comp + 1, self.part_list[ index_part + 1].component_list ))
                        except:
                            pass
                    print( "ayo: %d" % self.adjacent_part_counter )


