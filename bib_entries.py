#------------------------------------------     EXTRACT DATA FROM pdf_json -------------------------------------------------
#
# Insert ref_entries from json files into our database, 
# primary key(paper_id,ref_name), foreign key:(paper_id)
# we are going to have 5 columns: paper_id, ref_name, ref_text, latex, ref_type
#
#--------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import unicodedata
import re
import string
import csv
import os, json
import itertools
from joblib import Parallel, delayed
import collections
from collections import Counter,defaultdict,OrderedDict,namedtuple     
import mysql.connector  
from settings import DB_CREDS

cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)
cursor = cnx.cursor()

#get all json files from pdf_json folder
path_to_json = 'pdf_json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        paper_id = json_text['paper_id']

        for name in json_text['bib_entries']:
            ref_id = json_text['bib_entries'][name].get('ref_id','')
            title = json_text['bib_entries'][name].get('title','')
            ref_year = json_text['bib_entries'][name].get('year','')
            venue = json_text['bib_entries'][name].get('venue','')
            volume = json_text['bib_entries'][name].get('volume','')
            issn = json_text['bib_entries'][name].get('issn','')
            pages =  json_text['bib_entries'][name].get('pages','')
            do = json_text['bib_entries'][name]['other_ids'].get('DOI')
            if json_text['bib_entries'][name]['other_ids'].get('DOI') is None:
                other_ids = ''
            else:
                for j in do:
                    other_ids = ''.join(do)
            data_bib = (paper_id,name,ref_id,title,ref_year,venue,volume,issn,pages,other_ids)
            add_data = ("INSERT IGNORE INTO bib_entries "
                        "(paper_id,bib_name,ref_id,title,ref_year,venue,volume,issn,pages,other_ids)"
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            cursor.execute(add_data,data_bib)
            cnx.commit()
            authors = json_text['bib_entries'][name]['authors']
            if json_text['bib_entries'][name]['authors'] != []:
                for index,j in enumerate(authors):
                    first_name = json_text['bib_entries'][name]['authors'][index].get('first','')
                    middle = json_text['bib_entries'][name]['authors'][index]['middle']
                    if middle == []:
                        middle = ''
                    else:
                        for k in middle:
                            middle = ' '.join(middle)
                    last_name = json_text['bib_entries'][name]['authors'][index].get('last','')
                    suffix = json_text['bib_entries'][name]['authors'][index].get('suffix','')
                    author_data = (paper_id,name,first_name,middle,last_name,suffix)
            else:
                first_name = ''
                middle =  ''
                last_name = ''
                suffix = ''
                author_data = (paper_id,name,first_name,middle,last_name,suffix)  
            add_data = ("INSERT IGNORE INTO authors_bib "
                "(paper_id,bib_name,first_name,middle,last_name,suffix)"
                "VALUES (%s,%s,%s,%s,%s,%s)")
            #print("added into db")
            #print(data)
            cursor.execute(add_data,author_data)
            cnx.commit()

cursor.close()
cnx.close()  

                  


