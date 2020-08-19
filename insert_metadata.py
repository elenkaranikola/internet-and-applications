#------------------------------------------     EXTRACT DATA FROM METADATA.CSV -------------------------------------------------
#
#                                   our table has the same structrure as the csv file downloaded
#
#
#--------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import unicodedata
import re
import string
import csv
import json
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

df = pd.read_csv('metadata.csv',low_memory=False)
#fill all null cells
df.fillna(" ",inplace=True)

index=0
for i in df.loc[:,'cord_uid']:
    #if there is only the year given fill the rest date with year-1-1
    if len(df.loc[index,'publish_time']) == 4:
        year = df.loc[index,'publish_time']
        df.loc[index,'publish_time'] = year + '-1-1'
    #'pubmed_id is given in the database as int, make sure there are no empty spaces
    if df.loc[index,'pubmed_id'] == ' ':
        df.loc[index,'pubmed_id'] = 0

    #save tha extracted data in a tuple
    data = (df.loc[index,'cord_uid'],df.loc[index,'sha'],df.loc[index,'source_x'],df.loc[index,'title'],df.loc[index,'doi'],df.loc[index,'pmcid'],df.loc[index,'pubmed_id'],df.loc[index,'license'],df.loc[index,'abstract'],df.loc[index,'publish_time'],df.loc[index,'authors'],df.loc[index,'journal'],df.loc[index,'mag_id'],df.loc[index,'who_covidence_id'],df.loc[index,'arxiv_id'],df.loc[index,'pdf_json_files'],df.loc[index,'pmc_json_files'],df.loc[index,'url'],df.loc[index,'s2_id'])
    #insert our data into our database
    add_data = ("INSERT IGNORE INTO general "
                "(cord_uid , sha, source_x, title, doi, pmcid, pubmed_id, license, abstract, publish_time, authors, journal, mag_id, who_covidence_id, arxiv_id, pdf_json_files, pmc_json_files, url, s2_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(add_data,data)
    cnx.commit()
    index += 1

cursor.close()
cnx.close()
