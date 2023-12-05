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

    def remove_event_dupes( self, dupe_list ):
        return list( set( dupe_list ) )

    def find_valid_components( self ):
        part_counter = 0
        gear_counter = 0

        for index_part, part in enumerate( self.part_list ):
            print ( part.print_components())
            for index_comp, component in enumerate ( part.print_components() ):
                if component.isnumeric() == False and component != '.':

                    event_adder = []

                    line_data = [ -1, 0, 1 ]

                    for i in line_data:
                        try:
                            result = self.get_entire_number( self.part_list[ index_part + i].component_list[ index_comp - 1], index_comp - 1, self.part_list[ index_part + i].component_list )
                            if result.isnumeric(): event_adder.append( int( result ) )
                        except:
                            pass
                        try:
                            result = self.get_entire_number( self.part_list[ index_part + i].component_list[ index_comp ], index_comp, self.part_list[ index_part + i].component_list )
                            if result.isnumeric(): event_adder.append( int( result ) )
                        except:
                            pass
                        try:
                            result = self.get_entire_number( self.part_list[ index_part + i].component_list[ index_comp + 1], index_comp + 1, self.part_list[ index_part + i].component_list ) 
                            if result.isnumeric(): event_adder.append( int( result ) )
                        except:
                            pass
                    print (event_adder)

                    part_counter += sum( self.remove_event_dupes( event_adder ) )
                    if component == '*' and len( self.remove_event_dupes( event_adder ) ) == 2:
                        print('hello')
                        print (self.remove_event_dupes( event_adder ) )
                        gear_counter += ( self.remove_event_dupes( event_adder )[0] * self.remove_event_dupes( event_adder )[1] )

            print ( "part_counter:", part_counter )
            print ( "gear_counter:", gear_counter )
