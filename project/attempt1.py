import json
import httplib
import pprint as pp
import sqlite3

api_key = '52fppsddmrwecrwejqe6hm37'
main_url = 'api.crunchbase.com'
site_str = '/v/1/search.js?'


def initiate_connection(url):
	return httplib.HTTPConnection(url)
	
def send_query(conn, query, sql_connection):
	ex_fp = open('exceptions.txt', 'w')
	count, page, outputstr = 0, 0, ""
	done = False
	while (not done):
		page += 1
		sql_connection.commit()
		conn.request("GET", query+str(page))
		try:
			response = json.loads(conn.getresponse().read())
		except :
			ex_fp.write(json.dumps(response))
		if len(response['results']) == 0:
			done = True
			continue
		for entity in response['results']:
			if entity['namespace']=='person':
				name = "%s, %s" % (entity['last_name'], entity['first_name'])
			else :
				name = entity['name']
			try:
				count += 1
				sql_connection.execute('''INSERT INTO recs VALUES (?, ?, ?)''', (name, entity['permalink'],entity['namespace']))
				
			except :
				ex_fp.write(pp.pprint(response))

			

def main():
	output = 'simple_output.txt'
	cb_connection=initiate_connection(main_url)
	search_topic = "healthcare"
	sql_connection = sqlite3.connect(search_topic+".db")
	sql_connection.cursor()
	sql_connection.execute('''DROP TABLE IF EXISTS recs''')
	sql_connection.execute('''CREATE TABLE recs (name text, permalink text, namespace text)''')
	sql_connection.commit()
	query = "%squery=%s&api_key=%s&page=" % (site_str, search_topic, api_key)
	send_query (cb_connection, query, sql_connection)
	sql_connection.close()

if __name__ == '__main__':
	main()
	
	