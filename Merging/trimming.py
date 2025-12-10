import csv
"""
Meant for removing additional columns from the 24/25 season
"""

input_filename = 'merged_gw_24_25.csv'
output_filename = 'merged_gw_24_25_cleaned.csv'

with open(input_filename, encoding='utf-8') as infile:
    with open(output_filename,'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row[:42])

print('finito')
