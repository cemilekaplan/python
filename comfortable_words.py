'''
Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).

The word will always be a string consisting of only letters from a to z.

Write a program which returns True if it's a comfortable word or False otherwise.
'''

left_h = "q, w, e, r, t, a, s, d, f, g, z, x, c, v, b"
right_h = "y, u, i, o, p, h, j, k, l, n, m"
word = set(input("").lower())

if word - set(left_h) == set() or word - set(right_h) == set() :
  print(False)
else:
  print(True)