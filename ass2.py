team_members= int(input("Enter the team_members= "))
months_the_project= int(input("Enter the months_the_project= "))
monthly_salary= float(input("Enter the monthly_salary= "))
total_cloud_cost= float(input("Enter the total_cloud_cost= "))


Salary_cost= team_members*months_the_project*monthly_salary
Subtotal= Salary_cost+total_cloud_cost
VAT=Subtotal*0.14
Total=Subtotal+VAT

print(f"Salary Cost= {Salary_cost:.2f}")
print(f"Subtotal= {Subtotal:.2f}")
print(f"VAT= {VAT:.2f}")
print(f"Total= {Total:.2f}")