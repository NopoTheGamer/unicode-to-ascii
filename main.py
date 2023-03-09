def convert(toUnicode):
    userInput = input("Enter input to convert\n")
    if toUnicode:
        print(chr(int(userInput)))
    else:
        if len(userInput) > 1:
            print("Invalid input")
            return
        print(ord(userInput))


print("(1) ASCII to Unicode")
print("(2) Unicode to ASCII")
match (input("1 or 2\n")):
    case "1":
        convert(True)
    case "2":
        convert(False)
    case _:
        print("Invalid input")


