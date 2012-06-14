import csv

thefile = open("thedata.txt", "rb")
data = csv.DictReader(thefile, delimiter="\t")
nrows = 0
for row in data: # need to loop through to init the data for some weird reason
	nrows += 1
cols = data._fieldnames

thefile.seek(0)

counter = {}

for i, col in enumerate(cols):
	if col == "ROW No." or col == "ENGLISH": continue
	outercol  = cols[i]
	counter[outercol] = {}
	j = i + 1
	while j < len(cols):
		innercol = cols[j]
		#print outercol + ", " + innercol
		counter[outercol][innercol] = 0
		counter[outercol]['na'] = 0
		for row in data:
			# print row[outercol] + " " + row[innercol]
			if row[outercol] == "NA":
				counter[outercol]['na'] += 1


			colAterms = row[outercol].split(",")
			colBterms = row[innercol].split(",")

			for term in colAterms:
				if term in colBterms:
					counter[outercol][innercol] += float(1)/max([len(colAterms), len(colBterms)])

			#if row[outercol] == row[innercol] and row[outercol] != '':
				#if outercol == "ROW No.": print row[outercol].find('\n')
				#counter[outercol][innercol] += 1
		thefile.seek(0)
		print outercol + " to " + innercol + ": " + str(round(float(counter[outercol][innercol])/(nrows - counter[outercol]['na']) * 100))
		j += 1