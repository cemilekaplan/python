Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

The desired output is like :

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



x,y = 1,1 
z = 0
liste = [x,y]

while z < 55:
  
 
  z = x + y
  x = y
  y = z
  liste.append(z)

print(liste)
  
