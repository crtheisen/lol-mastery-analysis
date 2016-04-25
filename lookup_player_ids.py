import sys,requests
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

w = open("./data/players.csv","rU")
nameList = ""
nameList_length = 0

f = open("./data/player_ids.csv","w")

playerIDList = []
last_champ = 0

for line in w:
  line = line.split(",")
  last_champ = line[0]
  nameList += line[1].rstrip("\n") + ","
  nameList_length = nameList_length + 1
  if (nameList_length == 40):
    result = api.get_playerid_from_playername(nameList.rstrip(","))
    for info in result:
      f.write(str(last_champ) + "," + str(result[info]["id"]) + "\n")
    nameList = ""
    nameList_length = 0

if(nameList_length != 0):
    result = api.get_playerid_from_playername(nameList.rstrip(","))
    for info in result:
      f.write(str(last_champ) + "," + str(result[info]["id"]) + "\n")







