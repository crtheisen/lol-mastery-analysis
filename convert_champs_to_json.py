import sys
import csv
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

r = open("./data/champion_list.csv","rU")
csv_r = csv.reader(r)

f = open("./data/champion_list.json","w")

f.write("{\n")
f.write("  \"nodes\":[\n")

headers = False
for line in csv_r:
  if (headers):
    print line
    f.write("    {\n     \"name\": \"" + line[0] + "\",\n     \"graph_num\": " + line[2] + ",\n     \"id\":   " + \
      line[1] + ",\n     \"link\": \"http://www.mobafire.com/league-of-legends/champion/" + line[3] + \
      "-" + line[4] + "\",\n     \"img\":  \"http://ddragon.leagueoflegends.com/cdn/6.8.1/img/champion/" + line[5] + \
      ".png\",\n     \"group\": " + line[6] + "},\n")
  else:
    headers = True

f.write("  ]\n")
f.write("}\n")