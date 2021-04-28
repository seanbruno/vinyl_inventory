#!/usr/local/bin/python

import sys, getopt
import pandas as pd

def usage():
	print ('csv_to_html.py -h -i <input_csv> -o <output_html>')
	sys.exit(2)

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["help","input_csv=","output_html="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	input_csv = ''
	output_html = ''
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
		elif opt in ("-i", "--input_csv"):
			input_csv = arg
		elif opt in ("-o", "--output_html"):
			output_html = arg
		else:
			assert False, usage();


	# Open the CSV for conversion
	fd = pd.read_csv(input_csv)
	
	# Use the .to_html() to get your table in html
	print(fd.to_html(output_html, index=False, na_rep="", justify="center"))

if __name__ == "__main__":
	main(sys.argv[1:])
