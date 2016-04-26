import sys
sys.dont_write_bytecode = True

r = open("./data/affinity_table_normalized.csv","rU")

champion_list = open("./data/champion_list.csv","rU")

edge_force_graph = open("./data/champion_edge_force_graph.json", "w")

champion_dict = {}

headers = False
for champion in champion_list:
  if (headers):
    champion = champion.split(",")
    champion_dict[int(champion[2])] = champion[0]

  else:
    headers = True


edge_force_graph.write("{\n  \"links\":[\n")
for champion_id in range(0, 130):
  if (headers):
    temp_edge_string = ""
    line = r.next()
    line = line.split(",")
    myTop1 = sorted(range(len(line)), key=lambda i:float(line[i]))[129:]
    myTop1.reverse()
    for item in myTop1:
      edge_force_graph.write("    {\"source\":" + str(champion_id) + ",\"target\":" + str(item) + ",\"value\":1},\n")
      
  else:
    headers = True
edge_force_graph.write("  ]\n}")