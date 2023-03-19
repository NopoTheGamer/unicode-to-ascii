FUNCTION convertToUnicode():
  * ASK the user to enter an input to be converted
  * IF input is not a digit:
    * PRINT "Invalid input"
    * RESTART the program
  * CONVERT the input into a digit
  * IF the digit is under zero:
    * PRINT "Invalid input"
    * RESTART the program 
  * IF the digit is above 127:
    * PRINT that the digit isn't a part of ASCII, but it will be converted anyway
  * CONVERT digit to Unicode using the chr() function
  * PRINT the Unicode value
  * RESTART the program

FUNCTION convertToASCII():
  * ASK the user to enter an input to be converted
  * IF length of user input is larger than 1:
    * Initialise a new array to store the ASCII code points
    * FOR each char in user input:
      * CONVERT char to ASCII using the ord() function
      * ADD the ASCII value to the array
    * UNPACK the array
    * PRINT the unpacked array
    * RESTART the program
  * ELSE IF length of user input is zero:
    * PRINT Invalid input, you need to enter at least one character
    * RESTART the program
  * ELSE:
   * CONVERT char to ASCII using the ord() function
   * PRINT the ASCII value
   * RESTART the program

FUNCTION main():
  * PRINT (1) ASCII code point (integer) to Unicode representation
  * PRINT (2) Unicode representation to ASCII code point
  * PRINT (3) Exit
  * ASK the user to enter 1, 2 or 3
  * IF the input is 1:
    * CALL convertToUnicode()
  * ELSE IF the input is 2:
    * CALL convertToASCII()
  * ELSE IF the input is 3
    * CALL exit()
  * ELSE:
    * PRINT Invalid input
    * RESTART the program

CALL main()