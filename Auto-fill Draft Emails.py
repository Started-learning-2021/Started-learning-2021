from files import readCSV

if __name__ == '__main__':
  # Read the rows
  rows, fieldnames = readCSV('C:\\Users\\Ben\\Desktop\\Python\\Projects\\AutoEmail\\PersonalEmailsVHBA\\RHIF R5 Emails.csv')

import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("pythonemailer02@gmail.com", "Password1234@")
server.sendmail("pythonemailer02@gmail.com", "healthservice@gmail.com", "email body")

server.quit()
