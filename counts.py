import csv

data = csv.DictReader(open("thedata.txt", "rb"), delimiter="\t")

counter = 0

for row in data:
	for outercol in row:
		for innercol in row:
			if outercol != innercol:
				if row[outercol] == row[innercol]:
					counter += 1
print counter