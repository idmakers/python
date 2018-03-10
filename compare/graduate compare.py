import csv
import sys

orig_stdout = sys.stdout
f1 = open('source.csv', 'r')
f2 = open('des.csv', 'r')
f3 = open('results.txt', 'w')
sys.stdout = f3

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)
for hosts_row in c1:
    row = 1
    found = False
    for master_row in masterlist:
        if hosts_row[1] == master_row[1] :
            if found == True:
                print(master_row)
            else:
                print(hosts_row)
                print(master_row)
            if master_row[1] != "end":
                row = row + 1
                found = True





sys.stdout = orig_stdout

f1.close()
f2.close()
f3.close()
