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
This is a sample result from the search endpoint:
{"total": 1234,
 "page": 1,
 "crunchbase_url": "http://www.crunchbase.com/search?query=your_query",
 "results":
  [{"name": "Name of Entity",
    "category_code": null,
    "description": "Description of entity",
    "permalink": "permalink-of-entity",
    "crunchbase_url": "http://www.crunchbase.com/company/permalink-of-entity",
    "homepage_url": "",
    "namespace": "company",
    "overview": "Overview of company, possibly including mission statement, footprint, key industries, etc.",
    "image": null,
    "offices":
     [{"description": "type of office",
       "address1": "123 Main St",
       "address2": "",
       "zip_code": "12345",
       "city": "Nowhere",
       "state_code": "TX",
       "country_code": "USA",
       "latitude": null,
       "longitude": null}]},
  {"name": "Name of Entity2",
    "category_code": null,
    "description": "Description of entity2",
    "permalink": "permalink-of-entity",
    "crunchbase_url": "http://www.crunchbase.com/company/permalink-of-entity2",
    "homepage_url": "",
    "namespace": "financial-organization",
    "overview": "Overview of organization, possibly including mission statement, footprint, key industries, etc.",
    "image": null,
    "offices":
     [{"description": "type of office",
       "address1": "456 Main St",
       "address2": "",
       "zip_code": "67890",
       "city": "Somewhere",
       "state_code": "AB",
       "country_code": "USA",
       "latitude": null,
       "longitude": null}]},}
}
       