#------------------------------------------     EXTRACT DATA FROM pdf_json -------------------------------------------------
#
# Insert ref spans from json files into our database, 
# primary key(paper_id,ref_id), foreign key:(paper_id)
# we are going to have 6 columns: paper_id, paragraph_number,start_text, end_text, text_span, ref_id
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

        #get ref spans
        for spot, j in enumerate(json_text['back_matter']):
            if json_text['back_matter'][spot]['ref_spans'] != []:
                for count, k in enumerate(json_text['back_matter'][spot]['ref_spans']):
                    start = json_text['back_matter'][spot]['ref_spans'][count]['start']
                    end = json_text['back_matter'][spot]['ref_spans'][count]['end']
                    text = json_text['back_matter'][spot]['ref_spans'][count]['text']
                    ref_id = json_text['back_matter'][spot]['ref_spans'][count]['ref_id']
                    ref_data = (paper_id,spot,start,end,text,ref_id)
                    add_data = ("INSERT IGNORE INTO ref_span_back_matter "
                                "(paper_id,paragraph_number,start_text,end_text,text_ref,ref_id)"
                                "VALUES (%s,%s,%s,%s,%s,%s)")
                    cursor.execute(add_data,ref_data)
                    cnx.commit()

cursor.close()
cnx.close()