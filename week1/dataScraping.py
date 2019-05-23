import requests
from requests.exceptions import HTTPError
import json


# retrieve data from FRED API
def retrieve_data():
	# get all released econ data in json format
	params = {"api_key": "27cbff1814752ba2aa046855f6d4a162", "file_type": "json"}
	try:
		response = requests.get("https://api.stlouisfed.org/fred/releases", params)
		response.raise_for_status()
		# saved the released data, headers not included
		data = response.json()['releases']
		# formatted_data = json.dumps(data, indent=4, separators=(',', ': '))
		# print (formatted_data)

		# write to local
		with open('release_data.json', 'w') as outfile:
			json.dump(data, outfile, indent=4, separators=(',', ': '))


	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')
	else:
		print("Data successfully retrieved!")
	

def parse():

	output = open("release_data.csv", "w")
	with open('release_data.json') as f:
		data = json.load(f)
		for d in data:
			i_d = str(d["id"])
			start = d["realtime_start"]
			end = d["realtime_end"]
			name = d['name']
			press = str(d["press_release"])
			link = "None"
			notes = "None"
			# link notes may be empty/undefined
			try:
				link = d["link"]
				# prunning some special characters
				notes = d["notes"].replace("\r\n", " ")

				
			except:
				pass

			line = [i_d, start, end, name, press, link, notes]
			output.write(','.join(line) + '\n')
			
			

	output.close()

def main():
	# get data
	
	# retrieve_data()

	parse()




	



if __name__ == '__main__':
	main()