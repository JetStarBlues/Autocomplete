#!/usr/bin/python

import cgi, cgitb
import re

# Get the 'q' parameter out of the incoming Query String
q = cgi.FieldStorage()

# Our limited 'database' contains a few users
# with their username and full name
data = [
	{
		"user" : "amon",
		"name" : "N. Equalist"
	},
	{
		"user" : "android18",
		"name" : "Bad Ass"
	},
	{
		"user" : "ayeka",
		"name" : "Crown Princess of the Imperial Family of Jurai"
	},
	{
		"user" : "gaara",
		"name" : "Sandy"
	},
	{
		"user" : "goku",
		"name" : "Kakarot"
	},
	{
		"user" : "hiruma",
		"name" : "Yoichi Hiruma"
	},
	{
		"user" : "naruto",
		"name" : "The next Hokage"
	},
	{
		"user" : "rockLee",
		"name" : "Rock Lee"
	},
	{
		"user" : "ryoko",
		"name" : "Space Pirate Ryoko"
	},
	{
		"user" : "sakura",
		"name" : "S&S Forever"
	},
	{
		"user" : "sasuke",
		"name" : "Sasuke Uchiha"
	},
	{
		"user" : "vegeta",
		"name" : "Saiyan Prince"
	}
]

# Make sure that we print out the correct HTML header
print ("Content-type: text/html\n\n")

#print ( q['to'].value )  #stackoverflow.com/a/3582540/2354735

# Now we "search" through the data
regex = re.escape( q['to'].value )

for row in data:
	# Looking for users that match our auto-complete search
		# stackoverflow.com/a/14225664/2354735
		# stackoverflow.com/a/500870/2354735
	if ( re.search(regex, row["user"], re.IGNORECASE) is not None or 
	     re.search(regex, row["name"], re.IGNORECASE) is not None ):  
		
		print ( '<li id="' + row["user"] + '">' +
				'<img class="icon" src="icons/' + row["user"] + '.png"/>' +
				'<div id="uDetails">' +
				'<span id="username">' + row["user"] + '</span>' +
				'<span> : </span>' +
		    	'<span id="fullname">' + row["name"] + '</span>' +
		    	'</div></li>' )

#References
# http://docs.python.org/3/library/cgi.html
# http://docs.python.org/3/library/http.server.html
# 	#python -m http.server --cgi 8000
# http://www.tutorialspoint.com/python/python_reg_expressions.htm