#!/usr/bin/env python3

#########################
# Simple Slicer 0.1     #
# By                    #
# Mosaab Alzoubi        #
# Rima Alrahily         #
# Hasan Alasir          #
#########################

import os
import sys

ver = "0.1"

if len(sys.argv) < 2:
	print("-=-= SIMPLE SLICER %s =-=-\n\n	USAGE:\n \n	ss [File To Slice] [Variable to Slice for]\n	\n You should enter file to test." % ver)
	quit()
	
infile = sys.argv[1]
input = open(infile,"r").read().splitlines()
var = sys.argv[2]
for line in input:
	if (line.startswith(var) \
	or line.startswith(var + '.') \
	or '\t' + var + '.' in line \
	or ' ' + var + '.' in line \
	or ' ' + var in line \
	or '\t' + var in line \
	or '(' + var in line \
	or var + ')' in line \
	or '=' + var in line) \
	and not line[0] == '#':
		print(line)
