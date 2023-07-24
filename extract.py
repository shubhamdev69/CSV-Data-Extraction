#Importing modules 're' for working with regex and 'csv' for working with csv files
import re
import csv

clickData = open("clickData.csv", 'w')
clickData.write("event,adId,campaignID,xForwardedFor,stateID,cityID" + '\n') 
renderData = open("renderData.csv", 'w')
renderData.write("event,adId,campaignID,xForwardedFor,stateID,cityID" + '\n')

pattern = r"\s\w+:"
with open("7007-29thJuly-Mumbai", 'r') as file:
	csvreader = csv.reader(file, delimiter = ',')
	for row in csvreader:
		if (row[2] == ' event:CLICK'):
			x = re.sub(pattern, '', row[2])
			clickData.write(x)
			li = [row[6], row[7], row[18], row[50], row[51]] 
			for x in li:
				x = re.sub(pattern, ',', x)
				clickData.write(x)
			else:
				clickData.write('\n')


			#clickData.write (row[51].replace(' cityId:', ',') + '\n')

		if (row[2] == ' event:RENDER'):
			x = re.sub(pattern, '', row[2])
			renderData.write(x)
			li = [row[6], row[7], row[18], row[50], row[51]]
			for x in li:
				x = re.sub(pattern, ',', x)
				renderData.write(x)
			else:
				renderData.write('\n')
clickData.close()
renderData.close()
