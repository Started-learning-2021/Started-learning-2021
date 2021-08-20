from files import readCSV, writeCSV

if __name__ == '__main__':
  # Read the rows
  rows, fieldnames = readCSV('C:\\Users\\Ben\\Desktop\\Python\\Projects\\AutoEmail\\PersonalEmailsVHBA\\RHIF R5 Example HS List.csv')

  # Print all row data
  for row in rows:
    print(row)

  # Print only the ASX_code
  #for row in rows:
    #print(row['ASX_code'])

  # What will be written
  output = []

  for row in rows:

    recipient = 'Health Service Email'
    title = f"{row['Health Service Name']}" + " - VHBA - RHIF R5 - Grant Program Kick-Off Meeting Request"

    # Construct the email
    email = f"Dear {row['Health Service Name']} Representative,\n"\
    "My name is Ben McRae and I am contacting you regarding the RHIF R5 Grant Program you recently accepted.\n"\
    "The Victorian Health and Building Authority (VHBA) has received your signed letter and I can confirm the following details:\n"\
    f"{row['Health Service Name']} has been granted {row['Total Grant Values']} for {row['Number of Projects']} project(s) across {row['Number of Locations']} location(s).\n"\
    "I am employed by a consultancy named Ontoit which has been selected to oversee the RHIF R5 Grant Program.\n"\
    "As part of Ontoit's engagement my colleague Alex Krombholz and I will establish a kick-off meeting with you.\n"\
    "At this meeting we will cover the Grant Program remit, milestone date setting, monthly reporting, milestone claims and any specific questions you have. kick-off meetings are programmed to occur between 10 Sept - 10 Oct, 2021.\n"\
    "To assist me in establishing a meeting, please email back several dates and times within the kick-off period that you are available to attend a one hour meeting. Meetings usually run for 20-30 minutes. However, an hour is suitable for complex projects and questions.\n"\
    f"We will create a Microsoft Teams meeting based on your availability. Please invite other {row['Health Service Name']} staff and directors you believe will benefit from attending.\n"\
    "Congratulations on receiving RHIF R5 Grant funding. I look forward to working with you.\n"\
    "Please contact me or my colleague Alex if you have questions. Our contact details are in the email signatures below.\n"\
    "Best Regards,\n"\
    "Ben McRae" 
    
    # Add it to the output
    output.append({
      'Health Service Email' : recipient,
      'title': title, 
      'email': email 
    })

  # Write the email outputs
  writeCSV(output, ['recipient'], ['title'], ['email'], 'RHIF R5 Emails.csv')