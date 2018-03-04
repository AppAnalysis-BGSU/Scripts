awk 'NR==FNR{array[$1];next} !($3 in array)' pivot dataFile
