#Calculate compounding interest

print("How much money is currently in your account?")
principal = float(input("Enter current amount in savings account: "))

print("What do you estimate will be the yearly % earning on this investment? ")
annual_interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

print("How many times per year you will compound?")
compound = int(input('Enter times per year: '))

print("How many years will you be saving and investing? ")
years = int(input("Enter number of years (use whole numbers): "))

print("How much will you invest each month?")
monthly_investment = float(input("Enter monthly contribution amount: "))

#compound interest component
compound_interest = principal * (1 + annual_interest / compound) ** (compound * years)

#future value
future_value = monthly_investment * ((((1 + annual_interest / compound)) ** (compound * years)) + 1 / (annual_interest / years))

total_amount = compound_interest + future_value

total_amount = compound_interest + principal + future_value
for i in range(0, years):
    if total_amount == 0:
        total_amount = principal

print("At the end of", + years, "years you will have $", format(total_amount, ".2f"))






