import sys
sys.dont_write_bytecode = True

r = open("./data/affinity_table_normalized.csv","rU")

champion_list = open("./data/champion_list.csv","rU")

edge_bundling = open("./data/champion_edge_bundling.json", "w")

champion_dict = {}

headers = False
for champion in champion_list:
  if (headers):
    champion = champion.split(",")
    champion_dict[int(champion[2])] = champion[0]

  else:
    headers = True

edge_bundling.write("[\n")
for champion_id in range(0, 130):
  print champion_id
  if (headers):
    temp_edge_string = ""
    line = r.next()
    line = line.split(",")
    temp_edge_string += "{\"name\":\"" + champion_dict[champion_id] + "\",\"size\":" + \
      str(champion_id) + ",\"imports\":["
    edge_bundling.write(temp_edge_string)
    
    temp_edge_string = ""
    i = 0
    for entry in line:
      if float(entry) > .175:
        temp_edge_string += "\"" + champion_dict[i] + "\","
      i += 1

    if temp_edge_string == "":
      max_edge = ""
      max_val = float(0)
      j = 0
      for entry in line:
        if max_val < float(entry):
          print "updating to: " + champion_dict[j]
          max_val = float(entry)
          max_edge = champion_dict[j]
        j += 1
      temp_edge_string += "\"" + max_edge + "\","

    temp_edge_string = temp_edge_string.rstrip(",")
    temp_edge_string += "]},\n"
    edge_bundling.write(temp_edge_string)
      
  else:
    headers = True
edge_bundling.write("]")