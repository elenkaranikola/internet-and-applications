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

        for name in json_text['ref_entries']:
            text = json_text['ref_entries'][name].get('text','')
            latex = json_text['ref_entries'][name].get('latex','')
            ref_type =  json_text['ref_entries'][name].get('ref_type','')
            data = (paper_id,name,text,latex,ref_type)
            add_data = ("INSERT IGNORE INTO ref_entries "
                        "(paper_id,ref_name,ref_text,latex,ref_type)"
                        "VALUES (%s,%s,%s,%s,%s)")
            cursor.execute(add_data,data)
            cnx.commit()

cursor.close()
cnx.close()
