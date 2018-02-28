awk -F"," '{if ($1) print $1}' latest.csv

# Get Nth Line of a text file 
cat hashList.txt|awk '{print $1; exit}'
