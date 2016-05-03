import sys
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

f = open("./data/player_list_master_challenger.csv", "w")

result = api.get_challenger_league_playerlist()
for i in result["entries"]:
  f.write(i["playerOrTeamId"] + "\n")

result = api.get_master_league_playerlist()
for i in result["entries"]:
  f.write(i["playerOrTeamId"] + "\n")

