amount = float(input("What was the total bill? : $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? : "))
ppl = int(input("How many people to split the bill? : "))

tip = 1 + tip/100
t_amount = amount * tip         
#tip in percent then mul to find __% out amount then add that tip to amount so percent + 1 which will be same
ppa = "{:.2f}".format(round(t_amount / ppl,2)) 
# if use round only then in case of 33.6 it will print same not 33.60

print(f"Each person should pay : ${ppa}")

