'''
Skribbl Formatter - Formats a text file to be used as a custom Skribbl.IO word list

Josh Villanueva
'''
# Obtain text file to format
fileName = input("Enter the txt file location: ")
txtFile = open(fileName, "r")

# Creates the formated txt file to put formated words
formatedTxt = open("Formated.txt", "w+")

# Reads through the given txt file to format words into formated txt
if txtFile.mode == 'r':
    for line in txtFile:
        for word in line.split():
            formatedTxt.write(word + ", ")

# Closing the text files once finished
txtFile.close()
formatedTxt.close()
