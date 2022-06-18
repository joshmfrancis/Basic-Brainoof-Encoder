# input message to encode
input = input("Enter text: ")

# creates an empty list to store the ascii values for the program
ascii = []

# creates a loop to create the output from inputted text
for x in input:

    # appends the ascii values of each inputted character to the empty list
    ascii.append(ord(x))

# for every ascii value representation of a character in the list, make a "+", and add a "." at the end. (Basic representation of a Brainoof character output)
charRep = (y * "+" + "." for y in ascii)

# prints the output in Brainoof as unpacked data values and changes the default seperator " " to ">" for the purpose of moving the pointer on the cells to prepare for every new character.
print (*charRep, sep=">")