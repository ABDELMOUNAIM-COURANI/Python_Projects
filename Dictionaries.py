#a dictionary is like a capsule or book that stores variables
#and when we call a variable from that dictionary we get it's value
#these variables here act as key value pairs which means that
#the key is the variable name and the value is the value inside that
#variable, and pairs is both the variable and its value they for a pair.

Dictionary1 = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
#you can also use numbers instead of months' abbreviation
print (Dictionary1["Mar"])
#instead of this print statement we can put Dictionary1.get("Mar") and we will get the same thing
#or if we choose a value 
# such as "day" that is not in the dictionary we can use .get("day", "Invalid Value") it will print a the default value in the right
# we set such "invalid value" 
