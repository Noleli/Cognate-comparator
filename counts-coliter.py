import csv

thefile = open("thedata.txt", "rb")
data = csv.DictReader(thefile, delimiter="\t")
for row in data: pass # need to loop through to init the data for some weird reason
cols = data._fieldnames

thefile.seek(0)

counter = {}

for i, col in enumerate(cols):
	outercol  = cols[i]
	counter[outercol] = {}
	j = i + 1
	while j < len(cols):
		innercol = cols[j]
		#print outercol + ", " + innercol
		counter[outercol][innercol] = 0
		for row in data:
			# print row[outercol] + " " + row[innercol]
			if row[outercol] == row[innercol]:
				counter[outercol][innercol] += 1
		thefile.seek(0)
		print outercol + " to " + innercol + ": " + str(counter[outercol][innercol])
		j += 1