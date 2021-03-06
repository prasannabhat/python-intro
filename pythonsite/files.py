fw = open('workfile.txt', 'w')
f = open('sample.txt', 'r+')

# To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string or bytes object
# it’s your problem if the file is twice as large as your machine’s memory
# If the end of the file has been reached, f.read() will return an empty string ('').
# print (repr(f.read()))
print (f.read())

# f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string,
# and is only omitted on the last line of the file if the file doesn’t end in a newline
# if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n',
# a string containing only a single newline.
f.seek(0)
print()
print (f.readline())
print (f.readline())

# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
f.seek(0)
for line in f:
	print (line, end=' ')

# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().	

# f.write(string) writes the contents of string to the file, returning the number of characters written.
f = fw
f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)
f.write(s)

# f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file
# when in binary mode and an opaque number when in text mode.

# To change the file object’s position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point;
# the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 
# 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and 
# defaults to 0, using the beginning of the file as the reference point.

f = open('binary', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)     # Go to the 6th byte in the file

print (f.read(1))

f.seek(-3, 2) # Go to the 3rd byte before the end

print (f.read(1))

# In text files (those opened without a b in the mode string), only seeks relative to the beginning of the file are allowed 
# (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values are those returned from the f.tell(), 
# or zero. Any other offset value produces undefined behaviour.

# When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file. 
# After calling f.close(), attempts to use the file object will automatically fail.
f.close()

with open('sample.txt', 'r') as f:
    read_data = f.read()
    print (read_data)
print (f.closed)    