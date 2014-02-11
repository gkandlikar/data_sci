### API Info ###
The crunchbase api is located here: http://developer.crunchbase.com/io-docs

In my initial stages, I am using the "search" endpoint, since I primarily wanted to get a feel for the data.
I search for all entities on the crunchbase db which has a keyword "healthcare."

The api is also not very great. Some comments here: http://apievangelist.com/2013/03/16/using-the-crunchbase-api/

The api returns JSON data. See below for a sample result.

### iPython Notebook ###
When you are looking through my iPython notebook, you can ignore the first entry. In that I was processing results and writing output to file.

Use the second entry, with all the sql_connection objects

### healthcare.db ###
Since my file approach wasn't working great,  I started filing things to a SQLite db. It's working much better.

### R code ###
The R file contains a simple plot to visualize the data

### Sample API output ###
See sample.json.