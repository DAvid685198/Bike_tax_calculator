print("Vehicle Tax Calculator")

cc = float(input("Enter vehicle engine capacity (CC): "))

if cc <= 1000:
    tax_rate = 10000
elif cc <= 1500:
    tax_rate = 15000
elif cc <= 2000:
    tax_rate = 25000
elif cc <= 2500:
    tax_rate = 40000
elif cc <= 3000:
    tax_rate = 60000
else:
    tax_rate = 80000

print("Engine Capacity:", cc, "CC")
print("Estimated Vehicle Tax: Rs.", tax_rate)