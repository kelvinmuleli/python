# number =int(input("math:"))
#
# if number > 0:
#      print("The number is positive")
# elif number < 0:
#      print("The number is negative")
# elif number == 0:
#      print("Number is 0")
# else:
#     print("invalid input")


# chem = 90
# phyc = -77
#
# if chem > 0 and phyc > 0:
#     print("Both are positive")
# elif chem < 0 and phyc < 0:
#     print("Both are negative")
# else:
#     print("One is negative")



chem = 90
phyc = -77

if chem and phyc > 0:
    print("Both are positive")
elif chem or phyc < 0:
    print("Both are negative")
else:
    print("One is negative")