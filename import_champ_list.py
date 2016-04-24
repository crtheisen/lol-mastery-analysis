import sys
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

graph_numbers = 0
result = api.get_champion_list()
f = open("./data/champion_list_api.csv","w")
print result
for i in result["data"]:
  f.write(str(result["data"][i]["name"]) + "," + str(graph_numbers) + "," + str(result["data"][i]["id"]) + "\n")
  graph_numbers = graph_numbers + 1