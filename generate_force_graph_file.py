import sys
import csv
sys.dont_write_bytecode = True

import json

from riot_api import RiotAPI

#set up champions

r = open("./data/champion_list.csv","rU")
csv_r = csv.reader(r)

force_graph = open("./web/data/champion_edge_force_graph.json", "w")

force_graph.write("{\n")
force_graph.write("  \"nodes\":[\n")

headers = False
notFirst = False
for line in csv_r:
  if (headers):
    if (notFirst):
      force_graph.write(",\n")
    force_graph.write("    {\n     \"name\": \"" + line[0] + "\",\n     \"graph_num\": " + line[2] + ",\n     \"id\":   " + \
      line[1] + ",\n     \"link\": \"http://www.mobafire.com/league-of-legends/champion/" + line[3] + \
      "-" + line[4] + "\",\n     \"img\":  \"http://ddragon.leagueoflegends.com/cdn/6.8.1/img/champion/" + line[5] + \
      ".png\",\n     \"group\": " + line[6] + "}")
    notFirst = True
  else:
    headers = True

force_graph.write("\n  ],\n")
r.close()

#set up links

r = open("./data/affinity_table_normalized.csv","rU")

champion_list = open("./data/champion_list.csv","rU")

champion_dict = {}

headers = False
for champion in champion_list:
  if (headers):
    champion = champion.split(",")
    champion_dict[int(champion[2])] = champion[0]

  else:
    headers = True

notFirst = False
force_graph.write("  \"links\":[\n")
for champion_id in range(0, 130):
  if (notFirst):
    force_graph.write(",\n")
  line = next(r)
  line = line.split(",")
  myTop1 = sorted(range(len(line)), key=lambda i:float(line[i]))[129:]
  myTop1.reverse()
  #actually just one entry, need to use the loop logic though
  for item in myTop1:
    force_graph.write("    {\"source\":" + str(champion_id) + ",\"target\":" + str(item) + ",\"value\":1}")
  notFirst = True
      
force_graph.write("\n  ]\n}")