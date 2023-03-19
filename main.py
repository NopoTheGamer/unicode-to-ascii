# This is the function that does all the converting and printing
# It takes a boolean as a parameter to determine if it should convert to unicode representation or ASCII code point

def convertToUnicode():
    # The input has a new line so the user types on the next line instead of right after the prompt
    userInput = input("Enter input to convert\n")
    # If the user doesn't enter a digit the input is invalid and the program resets
    if not userInput.isdigit():
        print("Invalid input")
        main()
        return
    # Make a new variable that is the input as an integer for code cleanliness
    userInputDigit = int(userInput)
    # ASCII code points can't be under 0
    if userInputDigit < 0:
        print("Invalid input")
        main()
        return
    # ASCII code points also can't be over 127, but I'll be nice and still print what the unicode representation is
    if userInputDigit > 127:
        print("This number is not apart of the ASCII standard but I will still convert it to unicode for you")
    # The chr method converts an integer to it's unicode character and returns it
    print(chr(userInputDigit))
    # We go back to the main loop so the user doesn't have to restart the program
    main()


def convertToASCII():
    userInput = input("Enter input to convert\n")
    # If the user inputs more than one character, we need to convert each character to it's ASCII code point
    if len(userInput) > 1:
        # Initialize a new array to store the ASCII code points
        strArray = []
        # We loop over the string which sets "i" to each character in the string
        for i in userInput:
            # Then we append the ASCII code point of the character to the array
            # The ord method returns an integer representing the Unicode character
            strArray.append(ord(i))
        # The funky lil "*" is called the splat operator, and it removes the brackets and commas from the array
        # [1, 2, 3] -> 1 2 3
        print(*strArray)
        main()
    # Obviously if the user doesn't enter anything, we can't convert it
    elif len(userInput) == 0:
        print("Invalid input, you need to enter at least one character")
        main()
    # Otherwise we can just print it like this
    print(ord(userInput))
    main()


def main():
    # Print a newline to make the program look nicer after converting something
    print("\n")
    print("(1) ASCII code point (integer) to Unicode representation")
    print("(2) Unicode representation to ASCII code point")
    print("(3) Exit")
    # Match statements are nicer than writing an if else chain
    match (input("1, 2 or 3\n")):
        case "1":
            convertToUnicode()
        case "2":
            convertToASCII()
        case "3":
            exit()
        # The "_" case is the default case, and it's used when none of the other cases match
        case _:
            print("Invalid input")
            main()


# We have to start the program somewhere
main()
