import sys
sys.dont_write_bytecode = True

r = open("./data/list_of_masteries.csv","rU")

f = open("./data/affinity_table_normalized.csv","w")

mastery_table = {}

expert_table = {}

affinity_table = {}

#read the whole mastery table into memory
headers = False
j = 0
for line in r:
  if (headers):
    lines = line.split(",")
    mastery_table[lines[0]] = []
    headers_2 = False
    for item in lines:
      if (headers_2):
        mastery_table[lines[0]].append(item.strip("\n"))
      else:
        headers_2 = True
  else:
    headers = True


for x in range(0, 130):
  expert_table[x] = []
  expert_count = 0
  for player in mastery_table:
    if int(mastery_table[player][x]) == 5:
      expert_table[x].append(player)
      expert_count += 1

  if expert_count == 0:
    expert_table[x].append("0")

for expert_list in expert_table:
  final_list = [0]*130
  for expert in expert_table[expert_list]:
    i = 0
    for item in mastery_table[expert]:
      final_list[i] += int(item)
      i += 1

  affinity_table[expert_list] = final_list
  

for row in affinity_table:
  affinity_table[row][row] = 0

for x in range(0, 130):
  for y in range(x, 130):
    affinity_table[x][y] += affinity_table[y][x]
    affinity_table[y][x] = affinity_table[x][y]

max_val = 0
for x in range(0, 130):
  for y in range(x, 130):
    if affinity_table[x][y] > max_val:
      max_val = affinity_table[x][y]

max_val = float(max_val)
print(max_val)

for x in range(0, 130):
  for y in range(x, 130):
    affinity_table[x][y] = float(affinity_table[x][y]/max_val)
    if affinity_table[x][y] > 1:
      affinity_table[x][y] = 1
    affinity_table[y][x] = affinity_table[x][y]


for row in affinity_table:
  temp = ""
  for col in affinity_table[row]:
    temp += (str(col) + ",")
  f.write(temp.rstrip(",") + "\n")

f.close()
