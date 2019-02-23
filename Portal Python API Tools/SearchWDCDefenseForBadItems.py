
# coding: utf-8

# This tool looks at a portal's items and gets descriptions of the items.

# In[1]:


from IPython.display import display
from arcgis.gis import GIS
#import os
import requests
from getpass import getpass
from datetime import datetime


# In the cell below, you will connect to your Portal for ArcGIS. 
# 
# <li> portal = the URL of the Portal "https://servername.domain.com/webadaptor"
# <li> username = an admin's user name
# <li> password = the password for that user

# In[2]:


portal = "https://wdcdefense.esri.com/portal"


# In[3]:


username = "jfwdcdefense"


# In[5]:


password = getpass()
gis = GIS(portal, username, password, verify_cert=True)


# Gets usernames.

# In[6]:


gisusers = gis.users.search()
#gisusers


# If you do not want users to have their content listed, then you can manual write their username in the list below.

# In[7]:


ignore_list = ['system_publisher', 'esri_nav', 'esri_livingatlas', 
               'esri_boundaries', 'esri_demographics','admin']


# In[ ]:


#temp_user_list = ['adrain', 'james_jones', 'jfwdcdefense']
#temp_user_list = ['john6807@AVWORLD']


# In the cell below, items in the featured gallery will listed and then items in the web maps will also be listed. 
# 

# In[9]:


source_items_by_id = {}
contains_list = 'Could not access any server machines. Please contact your system administrator.'
webappbuilder = ':3344/webappbuilder'
package = 'package'
data = 'data'


for user in gisusers:
    # time for eaxh user iteration
    startTime = datetime.now()
    
    if not user.username in ignore_list:  # ignore any 'system' Portal users
    #if user.username in temp_user_list:  # ignore any 'system' Portal users
        print ("===========================User================================")
        print("Collecting items for {}...".format(user.username))
        user_content = user.items(max_items=100000)
        
        # item ids from root folder first
        for item in user_content:
            #Do not try and ping None item.URL
            
            if (item.url is not None and webappbuilder not in item.url and package not in item.url and data not in item.url):
            #if (item.url is not None):
                try:
                    r = requests.get(item.url)
                    if contains_list in r.text:
                        #r = requests.get(item.url)
                        print("User = " +user.username)
                        print("Folder = root")
                        print("Item = "+item.title)
                        print("Type = " +item.type)
                        print("URL = " +item.url)
                        print ("Item URL = " + "https://wdcdefense.esri.com/portal/home/item.html?id=" + item.id)
                        print ("Server up, Service Not")
                        print("-------------------------Item-------------------------------")
                        continue
                                    #check for URLs that do not exist    
                except requests.exceptions.RequestException as e:  
                    print (e)
                    if e:
                        print("User = " +user.username)
                        print("Folder = root")
                        print("Item = "+item.title)
                        print("Type = " +item.type)
                        print("URL = " +item.url)
                        print ("Item URL = " + "https://wdcdefense.esri.com/portal/home/item.html?id=" + item.id)
                        print ('This is a bad url')
                        print("-------------------------Item-------------------------------")
                        #continue
                        pass
                    
                else:
                    #print ("Root")
                    pass

                        

                        
                #item ids from folders next
        folders = user.folders
        for folder in folders:
            folder_items = user.items(folder=folder['title'], max_items=10000)
            folder_title = folder['title']
            #if (item.url is not None and webappbuilder not in item.url and package not in item.url and data not in item.url):

            for item in folder_items:
                #source_items_by_id[item.itemid] = item
                if (item.url is not None and webappbuilder not in item.url and package not in item.url and data not in item.url):
                    try:
                        r = requests.get(item.url)
                        if contains_list in r.text:
                            #r = requests.get(item.url)
                            print("User = " +user.username)
                            print("Folder = "+folder_title)
                            print("Item = "+item.title)
                            print("Type = " +item.type)
                            print("URL = " +item.url)
                            print ("Item URL = " + "https://wdcdefense.esri.com/portal/home/item.html?id=" + item.id)
                            print (("Status Code = ") +str(r.status_code))
                            print ("Server up, Service Not")
                            print("-------------------------Item-------------------------------")
                            continue

                    except requests.exceptions.RequestException as e: 
                        print (e)
                        if e:
                            print("User = " +user.username)
                            print("Folder = "+folder_title)
                            print("Item = "+item.title)
                            print("Type = " +item.type)
                            print("URL = " +item.url)
                            print ("Item URL = " + "https://wdcdefense.esri.com/portal/home/item.html?id=" + item.id)
                            print ("This is a bad url")
                            print("-------------------------Item-------------------------------")
                            #continue  else:
                            #print("in folder " +folder_title)
                            pass

                    else:
                        #print ("in folder " +folder_title)
                        #print ("Folder / Item = "+folder_title + item.title)
                        continue
        
        print ("Completed bad item search for {}...".format(user.username))
        print (print("Time taken: " + str(datetime.now() - startTime)))
        print ("===========================User================================")

