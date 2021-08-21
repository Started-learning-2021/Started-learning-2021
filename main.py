import csv
from files import readCSV, writeCSV

#Create CSV file and Header before looping through the rows of and creating custom emails.
#The code below creates the correct header, but it is overridden by the below output. 

#header = ['Address', 'Title', 'Body']
#with open('RHIF R5 Emails.csv', 'a', newline='') as file:
  #writer = csv.writer(file, delimiter = ',')
  #writer.writerow([i for i in header])

if __name__ == '__main__':
  # Read the rows
  rows, fieldnames = readCSV('RHIF R5 Example HS List.csv')

  # Print all row data
  for row in rows:
    print(row)

  # Print only the ASX_code
  #for row in rows:
    #print(row['ASX_code'])

  # What will be written
  output = []

  for row in rows:

    recipient = row['Health Service Email']
    title = f"{row['Health Service Name']}" + " - VHBA - RHIF R5 - Grant Program Kick-Off Meeting Request"

    # Construct the email
    email = f"Dear {row['Health Service Name']} Representative,\n"\
    "\n"\
    "My name is Ben McRae and I am contacting you regarding the RHIF R5 Grant Program you recently accepted. The Victorian Health and Building Authority (VHBA) has received your signed letter and I can confirm:\n"\
    f" - {row['Health Service Name']} has been granted {row['Total Grant Values']} for {row['Number of Projects']} project(s) across {row['Number of Locations']} location(s).\n"\
    "\n"\
    "I am employed by a consultancy named Ontoit who is selected to oversee the RHIF R5 Grant Program on behalf of VHBA. As part of Ontoit's engagement my colleague Alex Krombholz and I will establish a kick-off meeting with you. This meeting will cover the Grant Program remit, milestone date setting, monthly reporting, milestone claims and any specific questions you have. kick-off meetings are programmed to occur between 10 Sept - 10 Oct, 2021.\n"\
    "\n"\
    "Please email back several dates and times within the kick-off period that you are available to attend a meeting for one hour. They usually run for 20-30 minutes. However, an hour is suitable for complex projects and questions.\n"\
    "\n"\
    f"I will create a Microsoft Teams meeting based on your availability. Please invite other {row['Health Service Name']} staff and directors you believe will benefit from attending.\n"\
    "\n"\
    "Please contact me or my colleague Alex if you have questions. Our details are in the email signatures below.\n"\
    "\n"\
    "Congratulations on receiving RHIF R5 Grant funding. We look forward to working with you.\n"\
    "\n"\
    "Best Regards,\n"\
    "Ben McRae" 
    
    # Add it to the output
    output.append({
      'recipient' : recipient,
      'title': title, 
      'email': email 
    })

  # Write the email outputs
  writeCSV(output, ['recipient', 'title', 'email'], 'RHIF R5 Emails.csv')