import sys
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

graph_numbers = 0
result = api.get_champion_list()

f = open("./data/champion_list_api.csv","rU")

api_dict = {}
labelRow = False
for i in f:
  i = i.split(",")
  if(labelRow):
    api_dict[i[0]] = i[1]
  else:
    labelRow = True

f.close()

f = open("./static/mobafire-icon-lookup.csv","rU")

final = open("./data/champion_list.csv","w")

final.write("Name,Riot_ID,Graph_ID,Mobafire_Name,Mobafire_ID,Image_ID,Cluster (MCL) (-i 3.4 -e 2)\n")
labelRow = False
for i in f:
  i = i.split(",")
  if(labelRow):
    final.write(i[0] + "," + api_dict[i[0]].rstrip("\n") + "," + i[1] + "," + i[2] + "," + i[3] + "," + i[4].rstrip("\n") + ",1\n")
    graph_numbers = graph_numbers + 1
  else:
    labelRow = True

f.close()
final.close()