# Import csv File

import csv
from Rankings import List 

Outputcsv = open('ASXListRankings.csv', 'w')
Outputcsv_header = ("ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap, ASX_Rankings")
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
        print(ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap, ASX_Rankings)

#Use Objects to create autotext

from ASX_Companies import ASX_Company
from Rankings import ASX_Rankings

Rank = ASX_Rankings(ASX_Code= " ")

for ASX_Company in ASX_Companies:
    print(ASX_Company.ASX_code, ASX_Company.Company_name, ASX_Company.Listing_date, ASX_Company.GICs_industry_group, ASX_Company.Market_Cap, ASX_Company.ASX_Rankings) 
    line = "{},{},{},{},{}""\n".format(ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap, ASX_Rankings)
    Outputcsv.write(line)
Outputcsv.close