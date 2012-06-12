import csv

data = csv.DictReader(open("thedata.txt", "rb"), delimiter="\t")

counter = 0

for row in data:
	sortedrow = sorted(row)
	for i, outercol in enumerate(sortedrow):
		j = i + 1
		while j < len(sortedrow):
			if row[sortedrow[i]] == row[sortedrow[j]]:
				counter += 1
			j += 1
print counter