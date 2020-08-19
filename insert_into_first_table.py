#------------------------------------------     EXTRACT DATA FROM pdf_json -------------------------------------------------
#
# this is the first table that we'll use to store our data, this table will have the primary key that is the paper id and a second 
# column containing the title
#
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
   
#establish a connection with the database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)
cursor = cnx.cursor()

#get all files from the pdf_json folder
path_to_json = 'pdf_json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

#this table will have two columns: paper_id, title and primary key:paper_id
first_table = pd.DataFrame(columns=['paper_id','title'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        paper_id = json_text['paper_id']
        title = json_text['metadata']['title']

        #fill our Dataframe
        first_table.loc[index] = [paper_id,title]

#inser into our database
index = 0
for i in first_table.loc[:,'title']:
    data = (first_table.loc[index,'paper_id'],first_table.loc[index,'title'])
    add_data = ("INSERT IGNORE INTO first_json "
                "(paper_id,title)"
                "VALUES (%s,%s)")
    cursor.execute(add_data,data)
    cnx.commit()
    index += 1

cursor.close()
cnx.close()

