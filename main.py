print("Hello this is your mortgage calculator! This calculator is made, so you don't have to calculate, how much you have to pay off on your house each month.")

home_price = input("Please tell me how much the house costs: ")
down_payment = input("How much money do you start with to pay off: ")
years = input("Now I want you to say how many years you have to pay off on the loan: ")
interest = input("Last but not least, tell me the interest percentage of your loan: ")
    
home_price = float(home_price)
down_payment = float(down_payment)
years = int(years)
interest = float(interest)

netto_mortgage = home_price - down_payment
    
monthly_interest = interest/12/100
months = years*12
monthly_payment = netto_mortgage* (monthly_interest*(1+monthly_interest)**months) / ((1+monthly_interest)**months-1)
monthly_payment = int(monthly_payment)
print("You have to pay {x} off each month!".format(x=monthly_payment))