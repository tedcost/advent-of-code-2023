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

    def find_valid_components( self ):
        for index_part, part in enumerate( self.part_list ):
            for index_comp, component in enumerate ( part.print_components() ):
                if component.isnumeric() == False and component != '.':
                    
                    # Previous Line
                    if ( index_part - 1 ) >= 0:
                        try:
                            print( self.part_list[ index_part - 1].component_list[ index_comp - 1], end="" )
                            if ( self.part_list[ index_part - 1].component_list[ index_comp - 1] ).isnumeric():
                                self.adjacent_part_counter += int( self.part_list[ index_part - 1].component_list[ index_comp - 1] )
                        except:
                            pass
                        try:
                            print( self.part_list[ index_part - 1].component_list[ index_comp ], end="" )
                            if ( self.part_list[ index_part - 1].component_list[ index_comp ] ).isnumeric():
                                self.adjacent_part_counter += int( self.part_list[ index_part - 1].component_list[ index_comp ] )
                        except:
                            pass
                        try:
                            print( self.part_list[ index_part - 1].component_list[ index_comp + 1])
                            if ( self.part_list[ index_part - 1].component_list[ index_comp + 1] ).isnumeric():
                                self.adjacent_part_counter += int( self.part_list[ index_part - 1].component_list[ index_comp + 1] )
                        except:
                            pass

                    # Current Line
                    try:
                        print( part.component_list[ index_comp - 1], end="" )
                        if ( part.component_list[ index_comp - 1] ).isnumeric():
                            self.adjacent_part_counter += int( part.component_list[ index_comp - 1] )
                    except:
                        pass
                    try:
                        print( part.component_list[ index_comp ], end="" )
                    except:
                        pass
                    try:
                        print( part.component_list[ index_comp + 1] )
                        if ( part.component_list[ index_comp + 1] ).isnumeric():
                            self.adjacent_part_counter += int( part.component_list[ index_comp + 1] )
                    except:
                        pass

                    # Future Line
                    if ( index_part + 1 ) <= len( self.part_list ):
                        try:
                            print( self.part_list[ index_part + 1].component_list[ index_comp - 1], end="" )
                            if ( self.part_list[ index_part + 1].component_list[ index_comp - 1] ).isnumeric():
                                self.adjacent_part_counter += int( self.part_list[ index_part + 1].component_list[ index_comp - 1] )
                        except:
                            pass
                        try:
                            print( self.part_list[ index_part + 1].component_list[ index_comp ], end="" )
                            if ( self.part_list[ index_part + 1].component_list[ index_comp ] ).isnumeric():
                                self.adjacent_part_counter += int( self.part_list[ index_part + 1].component_list[ index_comp ] )
                        except:
                            pass
                        try:
                            print( self.part_list[ index_part + 1].component_list[ index_comp + 1] )
                            if ( self.part_list[ index_part + 1].component_list[ index_comp + 1] ).isnumeric():
                                self.adjacent_part_counter += int(  self.part_list[ index_part + 1].component_list[ index_comp + 1] )
                        except:
                            pass
                    print( "ayo: %d" % self.adjacent_part_counter )
