days = int(input("Enter number of days: "))
day_of_week = input("The first day of the week: ")

print("{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}".format("Su","M","T","W","Th","F","S"))

for d in range(1, days + 1):
  print("{:3}".format(d),end="")
  if (d %  7 == 0):
    print()