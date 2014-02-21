### API Info ###
The crunchbase api is located here: http://developer.crunchbase.com/io-docs

The api is also not very great. Some comments here: http://apievangelist.com/2013/03/16/using-the-crunchbase-api/

The api returns JSON data. See below for a sample result.

### iPython Notebook ###

Click here to access the pretty version: 
http://nbviewer.ipython.org/github/gkandlikar/data_sci/blob/master/project/crunchbase.ipynb?create=1

#### Entries ####


* 1: 	Ignore this one
* 2: 	This is used to connect to the 'search' endpoint. 
		I search for entities in the crunchbase database 
		with a keyword of 'healthcare.' Then file the entity
		info into healthcare.db. You can use this db file in
		R to generate the plot.
* 3: 	This is used to connect to the "companies" endpoint
		I then extract the page of the company 'locu'.
* 4:	Repeat #3 with apple
* 5:	Repeat #4 with zephyr-health
* 6:	Connect to the Entity List endpoint and get all the records of the type 'company'
		File the info to companies.db

### healthcare.db ###
Since my file approach wasn't working great,  I started filing things to a SQLite db. It's working much better.

### companies.db ###
This is a SQLite db which holds a table with all the companies.
The columns are: company name, the permalink, the category (as identified by the company).
I currently exclude all companies where the category is null.

### R code ###
The R file contains some sample code for connecting to companies.db, and making a couple of plots.

### Visualizations ###
See visualizations folder

### Sample API output ###
See samples folder