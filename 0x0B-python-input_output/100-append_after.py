#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
	"""
	append_after -  inserts a line of text to a file
	after each line containing a specific string
	Args:
	    filename: name of file
	    search_string: the string to search
	    new_string: the string to append
	"""
	read_lines = []
	with open(filename, "r", encoding="utf-8") as f:
		read_lines = f.readlines()
		i = 0
		while i < len(read_lines):
			if search_string in read_lines[i]:
				read_lines[i:i + 1] = [read_lines[i], new_string]
				i += 1
			i += 1
	with open(filename, "w", encoding="utf-8") as file:
		file.writelines(read_lines)
