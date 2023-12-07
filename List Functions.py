lucky_numbers = [12,15,69,15,57,47,89,96]
bluds = ["lalo salamanca", "walter white","walter white","gus fring","mike","saul goodman"]
bluds2 = bluds.copy()
bluds.append ("hank")
bluds.insert (5,"blud")
bluds.remove ("hank")
#blud.clear () without anything between the () and it
#will remove everything from the list
bluds.pop (2) #can take one argument and if left with no argument
#between () it will remove the last elemnet in the list
#blud.index ("argument" or argument like numbers) returns
#the index number of the argument withing the list
lucky_numbers.count (15) #returns how many times an argument appears in a list
bluds.sort ()#sorts arguments in an ascending order
lucky_numbers.reverse()#opposite of sort

print (lucky_numbers)
print (bluds)