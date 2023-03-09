FUNCTION convertToUnicode():
  * Ask the user to enter an input to be converted
  * IF input is not a digit:
    * PRINT "Invalid input"
    * RESTART the program
  * Convert the input into a digit
  * IF the digit is under zero:
    * PRINT "Invalid input"
    * restart the program 
  * IF the digit is above 127:
    * PRINT that the digit isn't a part of ASCII, but it will be converted anyway
  * CONVERT digit to Unicode using the chr() function
  * PRINT the Unicode value
  * RESTART the program

FUNCTION convertToASCII():
  * Ask the user to enter an input to be converted
  * IF length of user input is larger than 1:
    * Initialise a new array to store the ASCII code points
    * FOR each char in user input:
      * CONVERT char to ASCII using the ord() function
      * ADD the ASCII value to the array
    * UNPACK the array
    * PRINT the unpacked array
    * RESTART the program
  * ELSE IF length of user input is zero:
    * PRINT the user is a fucking idiot
    * RESTART the program
  * ELSE:
   * CONVERT char to ASCII using the ord() function
   * PRINT the ASCII value
   * RESTART the program

FUNCTION main():
  * PRIBT 