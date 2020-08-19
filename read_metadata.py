#------------------------------------------     EXTRACT DATA FROM METADATA.CSV -------------------------------------------------
#
#                                   Plot tha number of articles per month the magazine "PLoS One" publishes
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
import matplotlib.pyplot as plt
   
#establish a connection with the database
cnx = mysql.connector.connect(
    host = DB_CREDS['host'],
    user = DB_CREDS['user'],
    passwd = DB_CREDS['pass'],
    database = DB_CREDS['db']   
)
cursor = cnx.cursor()

df = pd.read_sql('SELECT publish_time FROM general where journal = "PLoS One"', con=cnx)
Jan = 0
Feb = 0
Mar = 0 
Apr = 0 
May = 0 
Jun = 0 
Jul = 0 
Aug = 0
Sep = 0
Okt = 0 
Nov = 0
Dec = 0
for i in df['publish_time']:
    #month = i.month
    if i.month == 1: Jan +=1
    elif i.month == 2: Feb +=1
    elif i.month == 3: Mar +=1
    elif i.month == 4: Apr +=1
    elif i.month == 5: May +=1
    elif i.month == 6: Jun +=1
    elif i.month == 7: Jul +=1
    elif i.month == 8: Aug +=1
    elif i.month == 9: Sep +=1
    elif i.month == 10: Okt +=1
    elif i.month == 11: Nov +=1
    elif i.month == 12: Dec +=1

fig = plt.figure()
fig, ax = plt.subplots()
publications =[Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Okt, Nov, Dec]
ax.bar(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'],publications)
plt.show()

