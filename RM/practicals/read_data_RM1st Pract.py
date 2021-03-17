'''#importing csv files
import pandas as pd
mydata= pd.read_csv("C:\\Users\\HP\\Desktop\\apy.csv")
print(mydata)

-----------------
#if no header in the csv file
import pandas as pd
mydata1 = pd.read_csv("C:\\Users\\HP\\Desktop\\apy1.csv", header = None)
print(mydata1)

----------------------'''
''''#Add Column Names

import pandas as pd
df = pd.read_csv("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\sample.csv")
df["new_column"] = ""
df.to_csv("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\sample.csv", index=False)'''
------------------------------------------------------

import pandas as pd
df = pd.read_csv("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37\\sample.csv")
df["new_column"] = "abc"
df.to_csv("sample1.csv", index=False)
--------------------------'''
'''#importing from url
import urllib
from urllib.request import urlretrieve
import pandas as pd

url = 'http://winterolympicsmedals.com/medals.csv'
urlretrieve(url, 'medals.csv')

df_web = pd.read_csv('medals.csv')
print(df_web.shape)
df_web.head()
---------------------------------------'''
'''#importing from the database
import pymysql.cursors
import os
#os.chdir("6.0.0-alpha-community-nt-debug")
db=pymysql.connect("localhost","root","root","test")
print("connected")
cursor=db.cursor()

cursor.execute("select * from employee")
data=cursor.fetchall()
print(data)
db.close()
-----------------------------------'''
'''#reading the sheet names from an excel
import pandas as pd
import xlrd
data2=pd.ExcelFile("C:\\Users\\HP\\Desktop\\first.xls")
print(data2.sheet_names)
-------------------------------------------------'''
'''import pandas as pd
mydata = pd.read_table("C:\\Users\\HP\\Desktop\\foo1.txt")
print(mydata)
-------------------------------------------------'''
#following running with rdata library, though warning shown data displayed
import rdata
parsed=rdata.parser.parse_file(rdata.TESTDATA_PATH / "C:\\Users\\HP\\Desktop\\Research_Methodology_HSNC\\Practicals\\.RData")
converted = rdata.conversion.convert(parsed)
print(converted)
'''--------------------------------------------

#below code not working 
#http://www.sthda.com/english/wiki/saving-data-into-r-data-format-rds-and-rdata

import pyreadr
result=pyreadr.read_r("A_vector.RData")
# done! let's see what we got , 
print(result.keys()) # let's check what objects we got: there is only None
df1 = result[None] # extract the pandas data frame for the only object available






