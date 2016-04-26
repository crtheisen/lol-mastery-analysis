import sys
sys.dont_write_bytecode = True

f = open("./data/champion_list.csv","rU")
headers = False
for i in f:
  if (headers):
    i = i.split(",")
    sys.stdout.write("'" + i[0] + "',")
  else:
    headers = True