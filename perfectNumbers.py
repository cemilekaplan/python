'''
Try to find out if a number you get from the user is perfect.
A number is called a "perfect number" if the sum of its divisors is equal to itself. For example, 6 is a perfect number. (1 + 2 + 3 = 6)
'''

num = int(input(""))
total = sum([i for i in range(1,num) if num % i == 0])
if total == num :
  print("{} is a perfect number.".format(num))
else:
  print("{} is not a perfect number.".format(num))