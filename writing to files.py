#writing to files mean adding data to them like text for example...

employer_file = open ("employer2.txt", "w")

#when we add "w" we tell the the code to overwrite out data to the file which means
#to wipe out everything from that file and add our new data to that empty file
#and when we add "a" instead of "w" the code will add our data to the end of the existing data
#inside the file without deleting the existing data, but we should be careful and not
#run the code twice as it will add our data twice to the file which may mess up our
#external file especially when we deal with large sets of code.
#for example first time we run the code it will write data to the end of it
#but if we click run again it will write the same data next or under our
#previous output.

employer_file.write("\nBlud - The Hood Council President")

employer_file.close ()