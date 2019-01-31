annual_salary = float ( input ( "Enter your annual salary: " ) )
a = annual_salary
current_savings = 0
portion_deposit = 0.25
m_salary = annual_salary / 12
r = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
money_needed = total_cost * portion_deposit
months = 0
attempts = 0
low = 0
high = 1
guess = (high + low) / 2
while abs ( current_savings - money_needed ) >= 100:
    annual_salary = a
    m_salary = annual_salary / 12
    current_savings = 0
    months = 0
    while (months < 36):
        if (months % 6 == 0 and months != 0):
            annual_salary *= semi_annual_raise
        current_savings += m_salary * guess
        current_savings += current_savings * r / 12

        months += 1
    if (current_savings < money_needed):
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    attempts += 1
    if guess == 1:
        break
if guess == 1:
    print ( "you are not able to buy that house" )
else:
    print ( "you must save " + str ( guess ) + " each month to buy that house" )


