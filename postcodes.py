import sys

def postcodes():
	input_file = open("postcodes.csv","r")
	line_from_file = input_file.readline()
	while(line_from_file!=""):
		fields_from_line = line_from_file.split(",")
		postcode = str( fields_from_line[0] )
		suburb = str( fields_from_line[1] )
		state = str( fields_from_line[2] )
		sys.stdout.write("The postcode for "+str(suburb)+" is "+str(postcode)+" and is located in "+str(state)+".\n")
		line_from_file = input_file.readline()
	input_file.close()
	
postcodes()
