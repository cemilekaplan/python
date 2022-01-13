'''
To form a pascal triangle in Python, there is a stepwise in the software.
Firstly, an input number is taken from the user to define the number of rows.
Secondly, an empty list is defined, which is used to store values.
Then, a for loop is used to iterate from 0 to n-1 that append the sub-lists to the initial list.
'''

pascal = [[1]]
num = int(input("Number of iterations: "))
print(pascal[0]) # the very first row
for i in range(1,num+1):
    pascal.append([1]) # start off with 1
    for j in range(len(pascal[i-1])-1):
    # the number of times we need to run this loop is (# of elements in the row above)-1
        pascal[i].append(pascal[i-1][j]+pascal[i-1][j+1])
        # add two adjacent numbers of the row above together
    pascal[i].append(1) # and cap it with 1
    print(pascal[i])