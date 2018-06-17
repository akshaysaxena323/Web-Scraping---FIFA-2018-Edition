
# coding: utf-8

# ##### Importing URLlib packages

# In[44]:


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd


# ##### Replace URL from indianexpress.com for different game to extract the data into xls file

# In[45]:


url = 'https://indianexpress.com/section/fifa/schedules-fixtures/russia-vs-saudi-arabia-fifa-2018-21974-scorecard/'


# ##### Passing URL and reading/parsing content

# In[46]:


u_client = uReq(url)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html,"html.parser")


# ##### Finding list items in the page

# In[47]:


Headings_html = page_soup.findAll("div",{"class":"tops"})
Headings = Headings_html[0].findAll("li")

print(Headings[1])

stats_html = page_soup.findAll("div",{"class":"goal"})


# ##### Appending game fixtures and storing in arrays.

# In[48]:


i = 0
H_Team = []
A_Team = []
Event = []

for stat in stats_html:
    stats = stats_html[i].findAll("li")    
    H_Team.append(stats[0].text)
    Event.append(stats[1].text)
    A_Team.append(stats[2].text)
    i+=1
        
H_Team = list(map(int, H_Team))
A_Team = list(map(int, A_Team))


# ##### Exporting results to excel file

# In[55]:


df = pd.DataFrame({Headings[1].text:Event,Headings[0].text:H_Team,Headings[2].text:A_Team})
filename = Headings[0].text + ' VS '+Headings[2].text + '.xlsx'
writer = pd.ExcelWriter(filename, engine='xlsxwriter')
excelfile = df.to_excel(writer, sheet_name='Sheet1', encoding='utf8')
writer.save()

