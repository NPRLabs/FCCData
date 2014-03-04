import urllib
from datetime import date
import time
from sets import Set

"""Declaring the search variables"""
state = ''
call_sign = ''
city = ''

"""Save the results in a .txt file"""
def create_results(name,response,w_or_a):
	file = open(name,w_or_a)
	file.write(response)
	file.close()
		
"""Reads a .txt file.  Uses the list inside to make search."""
def list_search():

	print "Performing search..."
	
	source = 'testList.txt'
	
	notes = ''
	
	"""
	Enter 1 if searching by city.
	Enter 2 if searching by state.
	Enter 3 if searching by callsign.
	"""

	list_format = '2'
	
	"""Declaring the name of the file being created"""
	destination = 'cronResults.txt'
	
	list_file = open(source,"r")

	terms = list_file.read() #for the search log
	
	list_array = terms.split(",")
	
	list_file.close()
	
	old_results = open(destination,"r").read() #scanning through old document to compare to new results for changes.
	
	header = "|Callsign|Frequency|Service|Channel|Directional Antenna (DA) or NonDirectional (ND)|Hours of Operation for this record - Daytime, Nighttime, or Unlimited|FM Station Class|International Station Class|FM Status|City|State|Country|File Number (Application, Construction Permit or License) or Docket Number (Rulemaking)|Effective Radiated Power -- horizontally polarized  (maximum)|Effective Radiated Power -- vertically polarized  (maximum)|Antenna Height Above Average Terrain (HAAT) -- horizontal polarization|Antenna Height Above Average Terrain (HAAT) -- vertical polarization|Facility ID Number (unique to each station)|N (North) or S (South) Latitude|Degrees Latitude|Minutes Latitude|Seconds Latitude|W (West) or (E) East Longitude|Degrees Longitude|Minutes Longitude|Seconds Longitude|Licensee or Permittee|Kilometers distant (radius) from entered latitude, longitude|Miles distant (radius) from entered latitude, longitude|Azimuth, looking from center Lat, Lon to this record's Lat, Lon|Antenna Radiation Center Above Mean Sea Level (RCAMSL) - Horizontally Polarized - meters|Antenna Radiation Center Above Mean Sea Level (RCAMSL) - Vertically Polarized - meters|Directional Antenna ID Number|Directional Antenna Pattern Rotation (degrees)|Antenna Structure Registration Number|Height of antenna radiation center above ground level (maximum) (physical center of the antenna)|Application ID number (from CDBS database)\n"
	
	create_results(destination,header,"w")
	
	if list_format == '1':
		for each in list_array:
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=&call=&city=' + each + '&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
			
			if response == '\n':
				print 'Nothing found using the search term "' + each + '".\n'
				notes = notes + 'Nothing found using the search term "' + each + '".\n'
			else:
				create_results(destination,response,"a")
		
	elif list_format == '2':
		for each in list_array:
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=' + each + '&call=&city=&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
		
			if response == '\n':
				print 'Nothing found using the search term "' + each + '".\n'
				notes = notes + 'Nothing found using the search term "' + each + '".\n'
			else:
				create_results(destination,response,"a")
			
	elif list_format == '3':
		for each in list_array:
		
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=&call=' + each + '&city=&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
	
			if response == '\n':
				print 'Nothing found using the search term "' + each + '".\n'
				notes = notes + 'Nothing found using the search term "' + each + '".\n'
			else:
				create_results(destination,response,"a")
	
	new_results = open(destination,"r").read()
	
	#put this if back in place when done debugging
	if old_results != new_results:
		changes = compare_results(old_results,new_results)
		notes = notes + "\nA change was made to the old data." + changes
		
	
	log_entry(source,terms,notes)
	
def compare_results(old,new):
	print "Comparing Results..." #there are 37 columns
	oldie = txt_to_array(old)
	newbie = txt_to_array(new)
	note = ""
	
	for oldRow in oldie:
		match = False
		for newRow in newbie:
			if newRow == oldRow:
				match = True
		if match == False:
			note = str(note) + "\nA change has been made to the row for Facility ID " + str(oldRow[18])
	
	return note
	
	
def txt_to_array(txt):
	txt = txt.split("\n")
	for row in range(len(txt)):
		txt[row] = txt[row].split('|') #need to split by |
	return txt
	
	
			
def log_entry(name,list_array,note_log):
	
	print "Logging search..."
	
	file = open('search_log.txt',"r")#r+ opens the txt for both reading and writing
	
	text = file.read()
	
	text = '************************************\nSearch Date:  ' + date.today().isoformat() + '\nSeach Time:  '+ time.strftime("%I:%M:%S") + '\n\nSearch created using ' + name + '.\n' + 'Search Terms: ' + list_array + '\n\nNotes:\n' + note_log + '\n\n' + text
	
	file = open('search_log.txt',"w")
	file.write(text)
	
	file.close()

list_search()
