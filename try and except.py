#try and except are used to make out program stable. when we run the program It works
#by first trying to execute a block of code. If an error occurs while executing the code,
#the except block is executed instead.
#try will have my code and if that code runs and give a certain error
#i wwouldn't want my program to break and or show me a lot of line of error statments
#telling me there is an error, but i want my program to keep running and here comes
#the except statemnt where my program shows a specific things i wanted it to show
#when there is an error.

try:
    v = 10/0
    num = int(input("blud must type here: "))
    print (num)
except ZeroDivisionError as err:
    print (err)
#i can eliminate as,err,and err in the print statement and put "Divided by zero" only
#inside print and I will get "Divided by zero".
#err is a variable that works for ZeroDivisionError which is a built-in exception in python
# and this ZeroDivisionError exception tells us that it is an error and we can't
# divide by zero.
except:
    print ("Invalid Thoughts")
