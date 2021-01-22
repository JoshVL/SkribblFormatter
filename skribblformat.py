'''
Skribbl Formatter - Formats a text file to be used as a custom Skribbl.IO word list

Josh Villanueva
'''
# Removing Special Characters
def remChars(inWord):
    inWord = inWord.replace(',', '')
    inWord = inWord.replace('.', '')
    inWord = inWord.replace('!', '')
    inWord = inWord.replace('=', '')
    inWord = inWord.replace(';', '')
    inWord = inWord.replace(':', '')
    
    return inWord

# Main Function
def main():
    # Obtain text file to format
    fileName = input("Enter the txt file location: ")
    txtFile = open(fileName, "r")

    # Creates the formated txt file to put formated words
    formatedTxt = open("Formated.txt", "w+")

    # Reads through the given txt file to format words into formated txt
    if txtFile.mode == 'r':
        for line in txtFile:
            for word in line.split():
                # Remove special characters
                word = remChars(word)
                # Does not write to txt if formated word is now empty
                if not(word == ''):
                    formatedTxt.write(remChars(word) + ", ")

    # Closing the text files once finished
    print("\nFormatted words successfully. Please check Formated.txt for your formated list of words.")
    txtFile.close()
    formatedTxt.close()

if __name__ == "__main__":
    main()