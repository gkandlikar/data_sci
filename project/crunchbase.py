#connect to companies endpoint
#getting information about every single company and filing it into companies.db
import json
import httplib
import pprint as pp
import sqlite3
import codecs

API_KEY = open('/Users/gk/Desktop/github/keys/cb', 'r').read().strip()
OUTPUTDIR='/Users/gk/Desktop/data_sci/crunchbase/data'
URL = 'api.crunchbase.com'
COMPANIES_EL = '/v/1/companies.js?'
COMPANY_EI = '/v/1/company/'
EXCEPTION_FILE= ''.join((OUTPUTDIR,'/exceptions.txt'))


def initiate_connection(url):
	return httplib.HTTPConnection(url)

def generate_description_string(company_detail):
    return '\n'.join(filter(None, [company_detail[key] for key in ['overview', 'description', 'tag_list']]))

def get_company_overview(cb_conn,permalink):
    global COMPANY_EI, API_KEY, EXCEPTION_FILE
    cb_conn.request("GET",''.join((COMPANY_EI,permalink,'.js?api_key=',API_KEY)))
    return generate_description_string(json.loads(cb_conn.getresponse().read()))

def db_vals(conn, company):
    code = lambda x: x if x != '' else None
    name = company['name']
    permalink = company['permalink']
    cat = code(company['category_code'])
    descr = get_company_overview(conn, permalink)
    return permalink, name, cat, descr
    

def send_companies_query(conn, query, sql_connection):
    global EXCEPTION_FILE
    count = 0
    conn.request("GET", query)
    val = conn.getresponse().read().replace('][',',')
    response = json.loads(val)
    for company in response:
        try :
            sql_connection.execute('''INSERT INTO companies VALUES (?, ?, ?, ?)''', db_vals(conn,company))
            count += 1
            if count % 100 == 0 :
                sql_connection.commit()
                print "Count: %d" % count
        except :
            with codecs.open(EXCEPTION_FILE, 'a') as f:
                f.write('\n')
                f.write ('=======ERROR=======\n')
                f.write(json.loads(company))
    sql_connection.commit()

def setup_companies_table():
    global OUTPUTDIR
    sql_connection = sqlite3.connect(''.join((OUTPUTDIR,"/companies.db")))
    sql_connection.cursor()
    sql_connection.execute('''DROP TABLE IF EXISTS companies''')
    sql_connection.execute('''CREATE TABLE companies (permalink text primary key, name text, cat text, descr text)''')
    sql_connection.commit()
    return sql_connection
    
def companies():
    global URL, COMPANIES_EL, API_KEY
    cb_connection=initiate_connection(URL)
    sql_connection = setup_companies_table()
    query = "%sapi_key=%s" % (COMPANIES_EL, API_KEY)
    send_companies_query (cb_connection, query, sql_connection)
    cb_connection.close()
    sql_connection.close()

if __name__ == '__main__':
	companies()