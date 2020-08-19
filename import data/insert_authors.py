#------------------------------------------     EXTRACT DATA FROM pdf_json -------------------------------------------------
#
# this is the table will contain the authors of each paper, 
# primary key(paper_id,last_name), foreign key:(paper_id)
# we are going to have 12 columns named: paper_id,first_name,middle,last_name,suffix,laboratory,institution,postCode,settlement,region,country,email
# first we read the data from all the json files, save them in a dataframe, afterwards we insert them in our database
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

#get all files from the pdf_jason folder
path_to_json = 'pdf_json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

#authors table will have primary key:(paper_id,last_name) and foreign key:paper_id from the first_json table
#our table will then have as columns
first_table = pd.DataFrame(columns=['paper_id','title'])
authors = pd.DataFrame(columns=['paper_id','first_name','middle','last_name','suffix','laboratory','institution','postCode','settlement','region','country','email'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        paper_id = json_text['paper_id']

        #saving our data in a dataframe 
        spot = 0
        for j in json_text['metadata']['authors']:
            first_name = json_text['metadata']['authors'][spot].get('first','')
            middle = json_text['metadata']['authors'][spot]['middle']
            if middle == []:
                middle = ''
            else:
                for k in middle:
                    middle = ' '.join(middle)
            last_name = json_text['metadata']['authors'][spot].get('last','')
            suffix = json_text['metadata']['authors'][spot].get('suffix','')
            laboratory = json_text['metadata']['authors'][spot]['affiliation'].get('laboratory','')
            institution = json_text['metadata']['authors'][spot]['affiliation'].get('institution','')
            if json_text['metadata']['authors'][spot]['affiliation'].get('location') == None :
                postCode = ''
                settlement = ''
                region = ''
                country = ''
            else :
                postCode = json_text['metadata']['authors'][spot]['affiliation']['location'].get('postCode','')
                settlement = json_text['metadata']['authors'][spot]['affiliation']['location'].get('settlement','')
                region = json_text['metadata']['authors'][spot]['affiliation']['location'].get('region','')
                country = json_text['metadata']['authors'][spot]['affiliation']['location'].get('country','')
            email = json_text['metadata']['authors'][spot].get('email','')
            spot += 1
            data = (paper_id,first_name,middle,last_name,suffix,laboratory,institution,postCode,settlement,region,country,email)
            add_data = ("INSERT IGNORE INTO authors "
                "(paper_id,first_name,middle,last_name,suffix,laboratory,institution,postCode,settlement,region,country,email)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            #print("added into db")
            #print(data)
            cursor.execute(add_data,data)
            cnx.commit()

cursor.close()
cnx.close()      
#print("FINISHED READING!!!!!!!!!!!!")
##insert my data from the dataframe to my database
#index = 0
#for i in authors.loc[:,'first_name']:
#    data = (authors.loc[index,'paper_id'],authors.loc[index,'first_name'],authors.loc[index,'middle'],authors.loc[index,'last_name'],authors.loc[index,'suffix'],authors.loc[index,'laboratory'],authors.loc[index,'institution'],authors.loc[index,'postCode'],authors.loc[index,'settlement'],authors.loc[index,'region'],authors.loc[index,'country'],authors.loc[index,'email'])
#    for j in data:
#        print(j,type(j))
#    add_data = ("INSERT IGNORE INTO authors "
#                "(paper_id,first_name,middle,last_name,suffix,laboratory,institution,postCode,settlement,region,country,email)"
#                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
#    cursor.execute(add_data,data)
#    cnx.commit()
#    index += 1
#
#cursor.close()
#cnx.close()