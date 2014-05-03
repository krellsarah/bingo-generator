#!/usr/bin/python

import random, sys, getopt, pdfkit.pdfkit

# This function reads the bingo items from the input file, creates the bingo card, and outputs it to PDF. 
def doBingo(inputfile, outputfile, title, freespace_text):

	# Read input file and select 24 random items
	bingoItems = readFile(inputfile)
	if (len(bingoItems) < 24):
		print 'Too few items in input file. You need at least 24.'
	selected_items = random.sample(bingoItems, 24)

	# Create the HTML for the bingo card
	bingo_html = createBingoHtml(title, selected_items, freespace_text)	

	# Define settings for pdfkit
	options = {
	    'page-size': 'Letter',
	    'margin-top': '0.75in',
	    'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '0.75in',
	    'encoding': "UTF-8",
	}

	# Create pdf from the HTML string
	pdfkit.from_string(bingo_html, outputfile, options=options)

# Reads the bingo square items from the input file.
# the input file should be a simple text file with one item per line
def readFile(inputfile):
	try:
		lines = [line.strip() for line in open(inputfile, "r")]
		return lines
	except IOError:
		print 'There was an error opening the file ' + inputfile

# Creates the HTML representatin of the bingo card
def createBingoHtml(title, items, freespace_text):
	html_string = ""
	html_string += "<html>\n"
	html_string += "<table width='100%' height='100%' border='1px solid black' style='border-collapse: collapse' valign='middle' >\n"
	html_string += createTitleRow(title) + "\n"
	html_string += createBingoRow(items[0:5]) + "\n"
	html_string += createBingoRow(items[5:10]) + "\n"
	html_string += createBingoRow(items[10:12] + [freespace_text] + items[12:14]) + "\n"
	html_string += createBingoRow(items[14:19]) + "\n"
	html_string += createBingoRow(items[19:24]) + "\n"
	html_string += "</table>\n"
	html_string += "</html>\n"
	
	return html_string

# Creates the HTML for a single table row
def createBingoRow(row_items):
        row_html = "<tr>"
	for item in row_items:
		row_html += "<td align='center' width='20%' style='height: 7em;'>" + item + "</td>"
	row_html += "</tr>"
	return row_html

# Creates the HTML for the title row of the bingo table
def createTitleRow(title):
	header_html = "<tr>"
	for i in range(0, len(title)): 
		header_html += "<th style='padding: 36px 0px 0px 0px; height: 108px;'><h1><b>" + title[i] + "</b></h1></th>\n"
	header_html += "</tr>"
	return header_html

# Do validation on input and then call the function to make the bingo card. 
def main(argv):
	inputfile = ''
	outputfile = ''
	title = ''
	freespace_text = ''
	opts = list()
	args = list()
	try:
		opts, args = getopt.getopt(argv,"hi:o:t:f:")
	except getopt.GetoptError as e:
		print 'bingo.py -i <inputfile> -o <outputfile> -t <title> -f <freespacetext>'
	for opt, arg in opts:
		if opt == '-h':
			print 'bingo.py -i <inputfile> -o <outputfile> -t <title> -f <freespacetext>'
			print 'Both input file and output file are required.'
			print 'Title must be 5 characters'
			print 'Free space text is optional, as is title.'
		elif opt in ("-i"):
			inputfile = arg.strip()
		elif opt in ("-o"):
			outputfile = arg.strip()
		elif opt in ("-t"):
			title = arg.strip()
		elif opt in ("-f"):
			freespace_text = arg.strip()
	if(title != '' and len(title) != 5):
		print 'Title must be exactly 5 letters.'
		sys.exit(2)
	if(title == ''):
		title = "BINGO"
	if(freespace_text == ''):
		freespace_text = 'Free Space'
	if(inputfile != '' and outputfile != ''):
		doBingo(inputfile, outputfile, title, freespace_text)
	else: 
		print 'Both an input file and an output file are required. Try bingo.py -h for usage.'

if __name__ =='__main__':
    main(sys.argv[1:])








