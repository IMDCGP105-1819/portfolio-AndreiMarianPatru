annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream house: "))
portion_deposit=0.20
current_savings=0
m_salary=annual_salary/12
r=0.04
money_needed=total_cost*portion_deposit
months=0
while(current_savings<money_needed):
    current_savings+=m_salary*portion_saved
    
    current_savings+=current_savings*r/12
    
    months+=1
    
print(months)