import sys
sys.dont_write_bytecode = True

f = open("./data/affinity_table_normalized.csv","rU")

w = open("./web/data/heatmap_champs.tsv", "w")

w.write("row_idx\tcol_idx\taffinity\n")
row = 1
for line in f:
  line = line.split(",")
  col = 1
  for item in line:
    if(row == col):
      w.write(str(row) + "\t" + str(col) + "\t100\n")
    else:
      print(str(int(float(item)*100+0.5)))
      w.write(str(row) + "\t" + str(col) + "\t" + str(int(float(item)*100+0.5)) + "\n")
    col += 1
  row += 1