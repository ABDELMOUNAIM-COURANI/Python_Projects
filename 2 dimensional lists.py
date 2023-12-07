number_grid_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#think of the lists as a table with rows and colomuns
#so when [2][2] for examples we will get the number 9 which is in the index
#2 from the third list and the third colomun because we start from 0 meaning:
#[1,2,3], > this is 0
#[4,5,6], > this is 1 
#[7,8,9],  > this is 2
#[0] > this is 3
# 0|1|2
for row in number_grid_list:
    for col in row:
        print(col, end=" ")
        #end=" " put a space after each printed element or value
        #print() below tell the first for loop to jump to the next line
        #then continue printing
    print()