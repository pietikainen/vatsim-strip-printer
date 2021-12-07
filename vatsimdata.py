from aircraft import Aircraft
from urllib.request import urlopen
import json

url = 'https://data.vatsim.net/v3/vatsim-data.json'

# Store the responses
response = urlopen(url)
response2 = open('airlines.json', 'r')

# Read the JSON's
data = json.loads(response.read())
data2 = json.loads(response2.read())

# Define data extraction


def get_data():
    pilots = data['pilots']
    phonetic = data2['phonetic']
    # Store the user input
    print("\nPlease select the type of strips to collect and print: ")
    selection = input("Arrival or Departure? (a/d): ")
    if selection == "a":
        x = 'arrival'
    else:
        x = 'departure'

    strip = []
    for pilot in pilots:
        if pilot['flight_plan'] == None:
            continue
        # Try to get phonetic callsign from the airlines.json and add it to a variable.
        # If it's not in the database, then add an empty string
        if pilot['flight_plan'][x] == "EFHK":
            try:
                y = phonetic[pilot['callsign'][0:3]]
            except:
                y = ""
            # Fill the strip list with necessary data
            strip.append(Aircraft(pilot['callsign'],
                                  y,
                                  pilot['transponder'],
                                  pilot['flight_plan']['aircraft'],
                                  pilot['flight_plan']['remarks'],
                                  pilot['flight_plan']['deptime'],
                                  pilot['flight_plan']['altitude'],
                                  "sidstar",
                                  "rwy",
                                  pilot['flight_plan']['departure'],
                                  pilot['flight_plan']['arrival'],
                                  pilot['flight_plan']['enroute_time'],
                                  pilot['flight_plan']['route'],
                                  pilot['flight_plan']['flight_rules']
                                  ))
    return strip
