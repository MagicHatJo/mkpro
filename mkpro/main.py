#!/usr/bin/env python3

# Imports

import setup
import project_c

import remote

C_RED = "\033[31m"
C_RESET = "\033[0m"

# Dispatch table of current supported languages
dispatch = {
	"c": project_c.new
}

def main():
	#Setup
	args = setup.parse_args()
	try:
		setup.create_rootdir(args)

		#Dispatch to language specific setups
		dispatch[args.project_lang.lower()](args)
		
		#Git Setup
		remote.setup(args)

	except Exception as error:
		print(C_RED + "Error: " + C_RESET + str(error))
main()
