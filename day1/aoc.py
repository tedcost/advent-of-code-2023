import sys
import os
import logging
logger = logging.getLogger(__name__)

from aoc_app import AOC_App

# ------- 
if __name__ == '__main__':
	app=AOC_App()
	app.parse_args( sys.argv[1:] )
	app.validate_args()

	if app.run():
		sys.exit(0)
	else:
		sys.exit(1)
