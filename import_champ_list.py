import sys
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

result = api.get_champion_list()
for i in result["data"]:
  print str(result["data"][i]["id"]) + "," + str(result["data"][i]["name"])