import csv

data = csv.DictReader(open("thedata.txt", "rb"), delimiter="\t")

counter = {}

for row in data:
	sortedrow = sorted(row)
	for i, outercol in enumerate(sortedrow):
		j = i + 1
		counter[outercol] = {}
		while j < len(sortedrow):
			# colAterms = row[sortedrow[i]].split(",")
			# colBterms = row[sortedrow[j]].split(",")

			# for colAterm in enumerate(colAterms):
			# 	print colAterm

			#print colAterms

			if sortedrow[j] not in counter[outercol]: counter[outercol][sortedrow[j]] = 0
			if row[sortedrow[i]] == row[sortedrow[j]]:
				counter[outercol][sortedrow[j]] += 1
			j += 1
		
		print outercol + " to " + sortedrow[j] + ": " + str(counter[outercol][sortedrow[j]])