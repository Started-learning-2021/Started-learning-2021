# Import csv File

import csv
from typing import List 

Outputcsv = open('ASXListEmail.csv', 'w')
Outputcsv_header = ("ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap")
Outputcsv.write(Outputcsv_header)
with open('ASXList.csv', 'r') as f:
    myReader = csv.reader(f, delimiter=",")
    header = next(myReader)
    for row in myReader:
        ASX_code = row[0]
        Company_name = row[1]	
        Listing_date = row[2]
        GICs_industry_group	= row[3]
        Market_Cap = row[4]
        print(ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap)
        line = "{},{},{},{},{}""\n".format(ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap)
        Outputcsv.write(line)
Outputcsv.close
