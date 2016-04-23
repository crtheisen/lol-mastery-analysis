import sys
sys.dont_write_bytecode = True

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

argument = "Ellipson,T3lrec,Isomalt"

name_list = argument.split(",");
result = api.get_playerid_from_playername(argument)

id_list = []
id_dict = {}

for name in name_list:
  player_id = result[name.lower()]["id"]
  id_list.append(player_id)
  id_dict[player_id] = name.lower()


for player_id in id_list:
  result = api.get_championmastery_playerid_topcount(player_id, 2)
  print id_dict[player_id] + ":"
  for i in result:
    print str(i["championId"]) + "," + str(i["championPoints"])