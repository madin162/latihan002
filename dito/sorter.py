li = list()

#read line from file
#filename = 'songPlayCountAllTime.txt'
#filename = 'songPlayCountMonthlyTotal.txt'
filename = 'songPlayCountByUserTotal.txt'
with open (filename) as fin:
    for line in fin:
        kolom=line.split('\t')
        li.append(kolom)

#sort
sorted_li = list()
sorted_li = sorted(li, key=lambda x: int(x[1]), reverse=True)
#print sorted_li

#write to file
newfile = "sorted_" + filename
with open(newfile, 'w') as fout:
    for xli in sorted_li:
        fout.write(xli[0] + ',' + xli[1])
