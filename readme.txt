File Descriptions:

search.py:
-Python script which searches an FCC database and returns data
-Can search based on list or on individual data entry
-Can search based on call sign, city, or state

testList.txt:
-an example list to show the format required by search.py's list search.
 

Some features to consider adding.  The script should:

-Create an .xls (excel spreadsheet) file without manual assistance.
-look into checking for changes made to old results
-cron job to check a list of (call signs, states, etc), find the proper docket, check which have new info, only update the data for those
-keep a list of the public media stations from yesterday, check if any have changed since, update the info only on those that have changed
-check for updates after 3:30 AM to 4:30 AM every day (eastern time); this is when the files are updated according to http://transition.fcc.gov/mb/databases/cdbs/


Things to overcome with change checking:


-Ignore headers
-making a note to say what was changed and what it used to be (include dates); maybe but in a single changelog?
-making changes to the master .txt list
-what to do if a field is added?  This has happened 4 times since 2003
-save stuff to a variable first, and then add to a file all at once?
-turn the results into an array deliminated by "\n" on arrays deliminated by "|"
--the inner arrays should have 37 columns

1.  read 'yesterday's search'
2.  save to variable
3.  create 'today's search'
4.  compare 'today's search' to 'yesterday's search'
5.  log any differences in a dated running log.
6.