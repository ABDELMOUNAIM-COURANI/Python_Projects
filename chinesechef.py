from chef import chef

#we had to import chef file into the chinese chef file in order to inherit
#the chef's class functions and make them apply to our chinese chef file as well
#so instead of rewriting all of the functions in our chef file into the chinese chef file
#in order to use them, we inherited the functions with "from chef import chef" and "class chinese_chef (chef):"
#lines, therefore we can now use the functions inside chef file in the chinese chef file

class chinese_chef (chef):
    

    def make_special_dish(self):
        print ("the chef makes brown noodles")