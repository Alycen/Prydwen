print( "TEXT TO BINARY CONVERTER\n" )

text = raw_input("Please enter text to convert to binary.\n")
print(' '.join(format(ord(x), 'b') for x in text))
