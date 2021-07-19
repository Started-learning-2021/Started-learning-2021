# Import csv File

import csv 

with open("ASXList.csv", "r") as f:
    csvReader = csv.reader(f) 
    for row in csvReader:
        program = "SSMH"
        reporting = "monthly"

#automatic loop through all csv indexs to create mass custom emails. 
#This works. Now just need to get actual variables, fix wording and input proper csv file. Half way there.  

        print("VHBA - " + program + " Grant Program " + "- Kick-off Meeting " + "- " + row[0] + " ")
        print(" ")
        print("Dear " + row[0] + ", ")
        print(" ")
        print("My name is Ben McRae and I am contacting you on behalf of VHBA (the Victorian Health Building Authority) because I have been informed that your Health Service has been granted $" + row[4] + " funds under the " + program + " Grant Program. ")
        print(" ")
        print("I am from a consultancy called Ontoit, and am appointed to oversee the " + program + " Grant Program. I will work with you and your project team to assist in project reporting, milestone payment claims, scope proposals and questions you may have about the program. ")
        print(" ")
        print("I want to set up a 30 to 60 minute meeting with your project team next week. ") 
        print(" ")
        print("Please provide the name, email and contact number for the Project Team Members assigned to project delivery. This may be you and/or a number of others. ")
        print(" ")
        print("In our kick-off meeting we will cover the grant letter, your approved scope, " + reporting + " reporting, scope proposals and any of your questions. ")
        print(" ")
        print("Please inform me of at least two one hour slots you are available in the next 2 weeks so I can send a Microsoft Teams meeting to the project team. ")
        print(" ")
        print("Generally meetings are 20 to 60 minutes long. Please be aware that there is significant variance based on your Health Service and the scale and complexity of your approved projects.")
        print(" ")
        print("I look forward to working with you on your project(s). ")
        print(" ")
        print("Best Regards, ")
        print("Ben McRae")
        print(" ")
        print(" ")

#Output CSV Automatically to same directory as file
#Outputcsv = open('ASXListEmail.csv', 'w')
        #writer = csv.writer(Outputcsv)
        #writer.writerow(#output text)

#next step to connect to email and auto-draft using title and body and take an email cell to input that. Then draft and close email, not send.

