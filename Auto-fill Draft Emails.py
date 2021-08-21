import smtplib
from files import readCSV, writeCSV
from email.message import EmailMessage

if __name__ == '__main__':
  # Read the rows
  rows, fieldnames = readCSV('RHIF R5 Emails.csv')

  for row in rows:
    recipient = row['Address']
    subject = row['Title']
    body = row['Body']
    print(row)

Email_Address = "pythonemailer02@gmail.com"
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = Email_Address
msg['To'] = recipient 
msg.set_content(body)

#Want to auto attach say a PDF file, excel spreadsheet and a jpg file.  
#for file in files: 
  #with open(file, 'r+') as f: 
    #file_data = f.read()
    #file_name = f.name 

#587 is the Gmail server. To encrypt emails using this ID we need to specify below with smtplib: 
        #smtp.ehlo()
        #smtp.starttls()
        #smtp.ehlo()

#Not really sure what I am doing here want like to add several attachments from the same directory for each recipient: 
#Want to auto attach a PDF file, excel spreadsheet and a jpg file.  
#msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename = file_name)
 
#It seems the easier way to encrypt is to use the SMTP_SSL and #465 server ID instead of #587. Less code + encryption:
with smtplib.SMTP_SSL('smtp.gmail.com', '465') as smtp: 
    smtp.login("pythonemailer02@gmail.com", "Password1234@")
    smtp.send_message(msg)

    smtp.quit()

#What I haven't done is cycled through the csv file to create say 5 emails at once. 
