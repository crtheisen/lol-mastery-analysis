import sys
sys.dont_write_bytecode = True

#Generates the list of champions to be copy and pasted into web/heatmap.html
#updated for Python 3

f = open("./data/champion_list.csv","rU")
headers = False
notFirst = False
for i in f:
  if (headers):
    if (notFirst):
      sys.stdout.write(",")
    i = i.split(",")
    sys.stdout.write("'" + i[0] + "'")
    notFirst = True

  else:
    headers = True