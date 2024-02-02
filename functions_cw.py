def get_miles_driven():
  miles_driven = float(input("Enter miles driven: "))
  return miles_driven


def get_gallons_used():
  gallons_used = float(input("Enter gallons of gas used: "))
  return gallons_used


def get_cost_per_gallon():
  cost_per_gallon = float(input("Enter cost per gallon: "))
  return cost_per_gallon


def Bye():
  print("Bye!")


def main():
  miles_driven = get_miles_driven()
  gallons_used = get_gallons_used()
  cost_per_gallon = get_cost_per_gallon()
  if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
  elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
  else:

    mpg = miles_driven / gallons_used
    mpg = round(mpg, 1)

    TotalGasCost = round(gallons_used * cost_per_gallon, 1)
    cost_per_mile = round(TotalGasCost / miles_driven, 1)
    print()
    print("Miles Per Gallon: ", mpg)
    print("Total Gas Cost: ", TotalGasCost)
    print("Cost Per Mile: ", cost_per_mile)

    print()
    Bye()
if __name__ == "__main__":
  main()
