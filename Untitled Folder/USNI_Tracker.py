#-------------------------------------------------------------------------------
# Name:  Retrieve US Navy number of ships deployed
# Purpose: Goes to USNI and retrieves deployed ships per fleet
# Author:      John Fry
#               DC Technology Office, Defense Team
# Created:     1/30/18
# Copyright:   (c) john6807 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Modules


import  requests, string, csv
from lxml import html

csvFile = ("C:\\Dev\\Defense\\Readiness\\USNIShips.csv")

#Base Url where website resides
# Going to Parse URL string to allow for the date to be inserted

urlFMT = "https://news.usni.org/2018/01/22/usni-news-fleet-marine-tracker-jan-22-2018"

page = requests.get(urlFMT)
tree = html.fromstring(page.content)

#Total Force Ships for US Navy
TotalForcesTitle = tree.xpath('//div[@class="entry-content"]/h2[1]/text()')[0:]
TotalForcesNumber = tree.xpath('//div[@class="entry-content"]/h1/span/text()')[0:]

#Total Ships Underway
ShipsUnderway = tree.xpath('//div[@class="entry-content"]/table/tbody/tr/td/span/strong/text()')[0:3]
ShipsUnderwayNumbers = tree.xpath('//div[@class="entry-content"]/table/tbody/tr/td/span/b/text()')[0:3]

#Total Ships Deployed by Fleet
ShipsDeployed = tree.xpath('//div[@class="entry-content"]/table/tbody/tr/td/span/strong/text()')
ShipsDeployedByFleet = ShipsDeployed[3:4], ShipsDeployed[4:5], ShipsDeployed [6:7], ShipsDeployed[8:9], ShipsDeployed[10:11], ShipsDeployed[12:13], ShipsDeployed[14:]
ShipsDeployedByFleetList = list(ShipsDeployedByFleet)
ShipsDeployedByFleetFlatList= [item for ShipsDeployedByFleetList in ShipsDeployedByFleetList for item in ShipsDeployedByFleetList]
print (ShipsDeployedByFleetFlatList)


ShipsDeployedByFleetNumbers = tree.xpath('//div[@class="entry-content"]/table/tbody/tr/td/span/b/text()')[3:]

print (TotalForcesTitle)
print (TotalForcesNumber)
print (ShipsUnderway)
print (ShipsUnderwayNumbers)
print (ShipsDeployedByFleet)
print (ShipsDeployedByFleetNumbers)

headers = (TotalForcesTitle + ShipsUnderway + ShipsDeployedByFleetFlatList)
ships = (TotalForcesNumber + ShipsUnderwayNumbers + ShipsDeployedByFleetNumbers)
print (headers)
print (ships)

#Write units to csv file
with open(csvFile,'w') as file:
     writer = csv.writer(file,lineterminator="\n")
     writer.writerow(headers)
     writer.writerow(ships)


