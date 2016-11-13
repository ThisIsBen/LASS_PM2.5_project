from time import sleep
import sys
import json
import time
from datetime import datetime

#custom class
from airbox.querySiteID import querySiteID
from airbox.parseSite import parseSite



def main():
	cityList = ['taipei', 'newtaipei', 'taichung', 'tainan', 'kaohsiung']
	option = sys.argv[1]

	if option == '-q':
		print('>>> Query site ID: All')
		query = querySiteID(cityList)
		with open('siteID.json', 'w', encoding = 'UTF-8') as file:
			json.dump(query.queryID(), file)

	elif option == '-p':
		arg_city = sys.argv[2]
		database = 'AirBox_new'
		# add logfile to check the timestamp
		fp = open("../airbox_log/"+arg_city+"log", "a")
		
       
		


		with open('siteID.json') as file:
			data = json.load(file)

		#parse site data
		while True:
			
			#print start time
			start_time=datetime.now()
        	# print to logfile
			print (arg_city.capitalize()+" Start time: "+str(start_time), end="\n", file=fp)


			#start parser
			parse = parseSite(arg_city, data[arg_city], database)
			parse.parseData()
			


			# finish once
        	# print to logfile
			finish_time=datetime.now()
			print (arg_city.capitalize()+" Finish time: "+str(finish_time), end="\n", file=fp)

        	# sleep for 3 mins
			sleep(180)


if __name__ == '__main__':
	main()
