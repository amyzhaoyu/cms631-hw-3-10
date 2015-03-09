import csv, glob

files = glob.glob("CMS.631-s15-Favorite-Restaurants/*.csv")

for f in files:
	# read in files, write out to one large CSV (restaurants.csv)
	with open(f, "rU") as infile, open("restaurants.csv", "ab") as outfile:
	   reader = csv.reader(infile)
	   next(reader, None)  # skip the header row
	   writer = csv.writer(outfile)
	   for row in reader:
	       # process each row
	       writer.writerow(row)