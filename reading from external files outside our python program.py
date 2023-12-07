employer_file = open ("employer.txt", "r")

for emp in employer_file.readlines():
    print (emp)

#print(filename.readable()) when put in the code or inside the print statement
#it give us true or fales which is whether the file is there, readable or not
#and filename.readline() gives us the first line from the external file
#in case we wrote it twice like this:
#employer_file.readline()
#employer_file.readline()
#it will read the first and there is already the typing cursor is set to the second line
#and our interpreter reads the second readline() command, then it gives us the second line
#as well. or we can as much readline() commands to write as much lines we want
#or we can use employer_file.read() or readlines() with s to print the whole file
#if we add [] with a number between it next to readlines(), it
#  will give us the value in that index.
#or we can add the for loop to print all the lines

employer_file.close ()