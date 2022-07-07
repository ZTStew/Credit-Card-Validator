"""

Author: Zachary Stewart
Date: 07/07/2022

Description: Program takes a 14 digit long credit card number and checks if the number is valid.
Rules:
  Take the 1st, 3rd, 5th, 7th, 9th, 11th, 13th numbers and double each. If the value is more than 9, subtract 9, sum the values
  Take the 2nd, 4th, 6th, 8th, 10, 12th, 14th numbers and sum them
  Add together the 2 sums, if the result is a multiple of 10, the credit card number is considered valid.

Test values:
  12345678912325
  58667936100244

"""

flag = True
ccn = ""
even_sum = 0
odd_sum = 0

# loop ensures user enters a correct 14 digit credit card number
while flag:
  # try, except for handling unexpected user inputs
  try:
    # prompts user for credit card number (ccn)
    ccn = input("Input 14 digit credit card number: ")
    # attempts to cast 'ccn' to an int, if fails, there is a non-integer value in the user input
    int(ccn)
    # if 'ccn' is 14 long, basic number requirements confirmed, 'flag' set to 'False' to exit the loop
    if(len(ccn) == 14):
      flag = False
      print("14 digit long number provided:", ccn)

      # Loops through 'ccn'
      for i in range(len(ccn)):
        # if the number is an odd index (even count), add value to 'even_sum'
        if i % 2 == 1:
          # print("Even:", ccn[i])
          even_sum += int(ccn[i])
        # else, the number is an even index (odd count)
        else:
          # print("Odd:", ccn[i])
          # doubles value of index as 'odd_val'
          odd_val = int(ccn[i]) * 2
          # if 'odd_val' is greater than 10, subtract 9 from the value
          if odd_val > 9:
            odd_val -= 9
          # adds 'odd_val' to 'odd_sum'
          odd_sum += odd_val
      
      # print(even_sum)
      # print(odd_sum)

      # if 'even_sum' + 'odd_sum' is a multiple of 10, credit card number is valid
      if (even_sum + odd_sum) % 10 == 0:
        print("valid credit card number given")
      else:
      # if 'even_sum' + 'odd_sum' not a multiple of 10, credit card number is invalid
        print("Invalid credit card number given")

    elif(len(ccn) < 14):
      print("Credit Card number too short")
    else:
      print("Credit Card number too long")
      
  except:
    print("ERROR: Invalid Input")
    # if the length of ccn is 0, assume user wants to close program
    if(len(ccn) == 0):
      flag = False
