import logging
logger = logging.getLogger( __name__ )

class GetFileContents:

    def __init__( self, file_path ):

        self.file_path = file_path
        
    # ------- 
    def read_file( self ):
        with open( self.file_path ) as f:
            lines = f.readlines()

        return lines
