import operator
import sys
sys.dont_write_bytecode = True

f = open("./data/affinity_table_normalized.csv","rU")

champion_list = open("./data/champion_list.csv","rU")

w = open("./web/data/data_chart_champions.tsv", "w")

w.write("letter\tfrequency\n")

graph_dict = {}

champion_dict = {}

headers = False
for champion in champion_list:
  if (headers):
    champion = champion.split(",")
    champion_dict[int(champion[2])] = champion[0]

  else:
    headers = True

row = 0
for line in f:
  line = line.split(",")
  the_sum = 0.0
  for item in line:
    the_sum += float(item)
  graph_dict[row] = the_sum
  row += 1

sorted_list = sorted(graph_dict.items(), key=operator.itemgetter(1), reverse=True)
counter = 0
for item in sorted_list:
  if(counter == 65):
    w.close()
    w = open("./web/data/data_chart_champions_second.tsv", "w")
    w.write("letter\tfrequency\n")
  w.write(champion_dict[item[0]] + "\t" + "%.2f" % item[1] + "\n")
  counter += 1