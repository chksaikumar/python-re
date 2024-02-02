print("The Miles per Gallon program")
print()
miles_driven = float(input("Enter miles driven: "))  
gallons_used = float(input("Enter gallons of gas used: "))
cost_per_gallon = float(input("Enter cost per gallon: "))
if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    # cost_per_mile = cost_per_gallon / miles_driven
    mpg = miles_driven / gallons_used
    mpg = round(mpg, 1)
    # cost_per_mile = round(cost_per_mile, 2)
    TotalGasCost = round(gallons_used * cost_per_gallon,1)
    cost_per_mile = round(TotalGasCost / miles_driven, 1)
    print()
    print("Miles Per Gallon: ", mpg)
    print("Total Gas Cost: ", TotalGasCost)
    print("Cost Per Mile: ", cost_per_mile)
print("Bye!")
