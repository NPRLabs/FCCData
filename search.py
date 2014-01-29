import urllib
from datetime import date

"""Declaring the search variables"""
state = ''
call_sign = ''
city = ''
application_file_number = ''
service = 'FM' #only return FM, no FS or FA
record_types = ''
lower_frequency = '0.0'
upper_frequency = '107.9'
facility_id = ''
class_ = ''
docket_number = ''
list_type = '4'
radius = '' #In Kilometers
latitude_degrees = ''
latitude_minutes = ''
latitude_seconds = ''
north_south = 'N'
longitude_degrees = ''
longitude_minutes = ''
longitude_seconds = ''
east_west = 'W'
size = '9'

searching = 'yes'


"""Save the results in a .txt file"""
def create_results(name,response):
	file = open(name,"a")
	if response == '\n':
		file.write('Nothing found using your search terms.') 
	else:
		file.write(response)
	file.close()
	
"""Saves a .txt file that records all of the search terms used"""
def save_search(name,state,call_sign,city,url):
	new_name = 'search_for_'+name
	file = open(new_name,"w")
	
	file.write('Search used to create ' + name + '.\nDate:  ' + date.today().isoformat() + '\n\nURL: ' + url + '\n\n')
	if state != '':
		file.write('State: ' + state + "\n")
	if city != '':
		file.write('City: ' + city + "\n")
	if call_sign != '':
		file.write('Call Sign: ' + call_sign + "\n")
	file.close()

"""Enter the search terms in the python window"""
def window_search():
	"""Declaring the name of the file being created"""
	print '\nThe search results will be saved in a .txt file.\nIf you use the name of an existing file, the original will be overwritten.\n'
	destination = raw_input ( 'Destination File Name (Do not include extension):  ' ) + '.txt'
	
	"""Search Inputs"""

	print 'Press "Enter" to leave search variable blank.'
	state = raw_input ( 'State (AK, AL, AR, etc.): ' )
	call_sign = raw_input ( 'Call Sign (partial is fine): ')
	city = raw_input ('City (partial is fine): ')
	print '\nProcessing...\n'
	
	url = 'http://transition.fcc.gov/fcc-bin/fmq?state=' + state + '&call=' + call_sign + '&city=' + city + '&arn=' + application_file_number + '&serv=' + service + '&vac=' + record_types + '&freq=' + lower_frequency + '&fre2=' + upper_frequency + '&facid=' + facility_id + '&class=' + class_ + '&dkt=' + docket_number + '&list=' + list_type + '&dist=' + radius + '&dlat2=' + latitude_degrees + '&mlat2='+ latitude_minutes + '&slat2=' + latitude_seconds + '&NS=' + north_south + '&dlon2=' + longitude_degrees + '&mlon2=' + longitude_minutes + '&slon2=' + longitude_seconds + '&EW=' + east_west + '&size=' + size
	
	response = urllib.urlopen ( url ).read()
	
	create_results(destination,response)
	
	save = raw_input('\nSave a copy of the search terms used? (Type "yes" or "y")').lower()
	
	if save == 'yes' or save == 'y':
		save_search(destination,state,call_sign,city,url)
		
"""Reads a .txt file.  Uses the list inside to make search."""
def list_search():
	source = raw_input ( '\nList File Name (Do not include extension):  ' ) + '.txt'
	
	list_format = ''
	while list_format != '1' and list_format != '2' and list_format != '3':
		list_format = raw_input('\nEnter 1 if searching by city, 2 if searching by state, or 3 if searching by call sign.\n')
	
	"""Declaring the name of the file being created"""
	print '\nThe search results will be saved in a .txt file.\nIf you use the name of an existing file, the original will be overwritten.\n'
	destination = raw_input ( 'Destination File Name (Do not include extension):  ' ) + '.txt'
	
	print 'Processing...'
	
	list_file = open(source,"r")

	list_array = list_file.read().split(',')

	list_file.close()
	
	if list_format == '1':
		for each in list_array:
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=&call=&city=' + each + '&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
	
			create_results(destination,response)
		
	elif list_format == '2':
		for each in list_array:
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=' + each + '&call=&city=&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
		
			create_results(destination,response)
			
	elif list_format == '3':
		for each in list_array:
		
			url = 'http://transition.fcc.gov/fcc-bin/fmq?state=&call=' + each + '&city=&arn=&serv=FM&vac=&freq=0.0&fre2=107.9&facid=&class=&dkt=&list=4&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
	
			response = urllib.urlopen ( url ).read()
	
			create_results(destination,response)		
	
	
def create_search():
	"""Decide the type of search, either read from a list in a .txt file or take data entry"""
	print 'You may perform your search in one of two ways:  You can enter search terms here, or the terms can be read from a list.'
	
	search_type = '3'
	print 'Enter 1 to enter search terms here.\nEnter 2 to have the terms read from a list.\nEnter 3 to learn about the list format requirments.\n'
	
	while search_type == '3':
		search_type = raw_input()
	
		#make a while 3 statement?
		if search_type == '1':
			window_search()
		elif search_type == '2':
			list_search()
		elif search_type == '3':
			print '\nWhen searching by list, you can choose to search by city, state, or call sign.\nYou will be asked to choose one of the three.\nThe terms in the list should be separated by commas with no spaces, but partial terms are acceptable (for example: "GA,AL,SC,F").\n'
			print 'Please enter 1 to enter search terms or 2 to pull them from a list.'
			search_type = '3'
		else:
			print 'Please enter 1, 2, or 3.'
			search_type = '3'
	
while searching == 'yes' or searching == 'y':
	create_search()
	searching = raw_input('\nWould you like to perform another search? If so, type "yes" or "y"\n').lower()
	print '\n\n'