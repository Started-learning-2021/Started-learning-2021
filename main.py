from files import readCSV, writeCSV

if __name__ == '__main__':
  # Read the rows
  rows, fieldnames = readCSV('ASXList.csv')

  # Print all row data
  for row in rows:
    print(row)

  # Print only the ASX_code
  for row in rows:
    print(row['ASX_code'])

  # What will be written
  output = []

  for row in rows:
    # Construct the email
    email = f"Dear {row['Company_name']},\n"\
      "My name is Ben McRae...\n"\
      "I am from...\n"

    # Add it to the output
    output.append({
      'email': email
    })

  # Write the email outputs
  writeCSV(output, ['email'], 'ASXListEmail.csv')
